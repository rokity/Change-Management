from module.query import QueryBuilder
from module.scopus import Scopus
from module.query import SubQueryBuilder

#Test Query Builder Library
# query=QueryBuilder()
# query.addFieldRestriction("KEY")
# query.addWord("ciao")
# query.addBooleanOperator("AND")
# query.addWord("hello")
# print(query.to_str())
# print(query.to_str())
# query_2=QueryBuilder()
# query_2.addFieldRestriction("KEY")
# query_2.addWord("ciao")
# query_2.addBooleanOperator("AND")
# query_2.addWord("hello")
# query.concatenate_query(query_2,boolean_operator="AND")
# print(query.to_str())

# #Test Scopus API Library
# simple_query=QueryBuilder()
# simple_query.addFieldRestriction("KEY")
# simple_query.addWord("machine learning")
# scopus=Scopus("")
# result=scopus.execute_query(simple_query.to_str())
# print(result)