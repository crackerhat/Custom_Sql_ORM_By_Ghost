class Compiler:

    def compile_expression(self, expression):
        column_name = expression.column.key
        operator  = expression.operator

        sql = f"{column_name} {operator} ?"

        parameters = [expression.value]

        return sql, parameters

    def compile_select(self, table_name, expressions=None):
        sql = f"SELECT * FROM {table_name}"
        parameters = []

        if expressions:
            conditions = []
            #age > 20 , username = ghost
            for expression in expressions:
                condition_sql, condition_parameters = self.compile_expression(expression)

                conditions.append(condition_sql)
                parameters.extend(condition_parameters)

            sql += " WHERE " + " AND ".join(conditions)

        return sql, parameters

