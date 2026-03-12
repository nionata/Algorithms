'''
Store the values by the column in a dict
'''
class ScioTable:
    # def __init__(self, column_names: string[]):
    def __init__(self, column_names):
        """Constructor, creates a table with the given columns"""
        self.rows = 0
        self.columns = {}
        self.column_names = column_names
        for i, col in enumerate(self.column_names):
            self.columns[col] = (i, [])
    
    def insert_row(self, row):
        """Adds a row to the end of the table. Row will have the same length as the number of
        columns, and index i of the row corresponds to column i"""
        self.rows+=1
        for i, val in enumerate(row):
            self.columns[self.column_names[i]][1].append(val)

    def read(self, columns):
        """Prints to the console the desired column headers in the order given followed by
        the values of the provided columns. If columns is an empty array, prints all columns.
        Different rows must be separated by a new line and rows must be printed in order of
        insertion."""
        if not columns:
            columns = self.column_names
        out, col_out = [], []
        for i, col in enumerate(columns):
            out.append(col)
            col_out.append(self.columns[col][1])
            if i < len(columns)-1:
                out.append(' | ')
        out = ''.join(out)
        print(out)
        print('-'*len(out))
        for i in range(self.rows):
            row_out = []
            for j, col_vals in enumerate(col_out):
                row_out.append(str(col_vals[i]))
                if j < len(col_out)-1:
                    row_out.append(' | ')
            print(''.join(row_out))

    def slice(self, columns):
        """Returns a new ScioTable instance which only has the passed in columns."""
        new_table = ScioTable(columns)
        for i, col in enumerate(new_table.column_names):
            col_vals = self.columns[col][1]
            new_table.columns[col] = (i, col_vals)
        new_table.rows = self.rows
        return new_table

    def add_column(self, column):
        """Returns a new ScioTable instance with the additional new column to the table. For
        existing rows, values for this column should be set to 0. You can assume the column
        name doesn’t match any of the existing column names."""
        new_table = ScioTable(self.column_names+[column])
        new_table.columns = self.columns.copy()
        new_table.columns[column] = (len(self.column_names), [0]*self.rows)
        new_table.rows = self.rows
        return new_table

    def delete_column(self, column):
        """Returns a new ScioTable instance which removes the given column. You can assume
        the column always exists."""
        new_column_names = []
        for col in self.column_names:
            if col != column:
                new_column_names.append(col)
        new_table = ScioTable(new_column_names)
        new_columns = self.columns.copy()
        del new_columns[column]
        for i, col in enumerate(new_column_names):
            if col == column:
                continue
            col_val = new_columns[col][1]
            new_columns[col] = (i, col_val)
        new_table.columns = new_columns
        new_table.rows = self.rows
        return new_table

    def inner_join(self, table2, column):
        """Returns a new ScioTable instance with columns from this table and table2 for
        whenever there are records with matching values for the given column. There is only
        one shared column between the two tables, which is the given column. The ordering of
        the columns in the new table should be {self.columns - column}{column}{table2.columns
        - column}. See examples on the next page."""
        unsorted_m, unsorted_n = self.columns[column][1], table2.columns[column][1]
        m, n = sorted(unsorted_m), sorted(unsorted_n)
        i, j = 0, 0
        matches = []
        while i < len(m) and j < len(n):
            a, b = m[i], n[j]
            if a == b:
                matches.append(a)
                i+=1
                j+=1
                continue
            if a < b:
                i+=1
            else:
                j+=1
        m_row_idxs = set([unsorted_m.index(match) for match in matches])
        n_row_idxs = set([unsorted_n.index(match) for match in matches])

        new_column_names = [col for col in self.column_names if col != column] + [column] + [col for col in table2.column_names if col != column]
        new_table = ScioTable(new_column_names)

        # WIP - generate the output rows based on both cols
        # for m
        #     for j, col_vals in enumerate(col_out):
        #         row_out.append(str(col_vals[i]))
        #         if j < len(col_out)-1:
        #             row_out.append(' | ')
        return new_table