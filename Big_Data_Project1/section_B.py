
import matplotlib.pyplot as plt
import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import association_rules, apriori

"""
---------------------------------------------------------------------------------------
Question 1:  When to use Apriori algorithm 

It is used for mining frequent item-sets and devising association rules from a 
transactional database. The parameters “support” and “confidence” are used. 
Support refers to items’ frequency of occurrence; confidence is a conditional 
probability.

Question 2: What happens when we decrease the support level? Why?    
When we decrease the support level then, the association between the items is 
decreased. Because it will show us the similarity between the transactions.

Question 3:  What happens when we increase the confidence level? Why?  
When we increase the support level then, the association between the items is 
increase. Because it will show us the similarity between the transactions.

Taking the following example to understand:

 Support = (Transactions involving specific item)/(Total Transactions for all items)
 
 Here, support is directly proportional to no. of transaction involving specific item
 and indirectly proportional to no. of transaction involving all items. 
 
---------------------------------------------------------------------------------------
"""


df = pd.read_csv('BreadBasket_DMS.csv')
transaction_list = []
for i in df['Transaction'].unique():
    t_list = list(set(df[df['Transaction'] == i]['Item']))
    if len(t_list) > 0:
        transaction_list.append(t_list)

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

getCountList = []
te = TransactionEncoder()
te_ary = te.fit(transaction_list).transform(transaction_list)
df2 = pd.DataFrame(te_ary, columns=te.columns_)


"""
---------------------------------------------------------------------------------------
Question 4:  Rules are generated with a support level of 5%.
---------------------------------------------------------------------------------------
"""
frequent_itemSets = apriori(df2, min_support=0.01, use_colnames=True)

# Confidence Level = 90%
rules = association_rules(frequent_itemSets, metric='confidence', min_threshold=0.09)
getCountList.append(len(rules))
print("Rules generated at 90% Confidence:  " + str(len(rules)))

# Confidence Level = 80%
rules = association_rules(frequent_itemSets, metric='confidence', min_threshold=0.08)
getCountList.append(len(rules))
print("Rules generated at 80% Confidence:  " + str(len(rules)))

# Confidence Level = 70%
rules = association_rules(frequent_itemSets, metric='confidence', min_threshold=0.07)
getCountList.append(len(rules))
print("Rules generated at 70% Confidence:  " + str(len(rules)))

# Confidence Level = 60%
rules = association_rules(frequent_itemSets, metric='confidence', min_threshold=0.06)
getCountList.append(len(rules))
print("Rules generated at 60% Confidence:  " + str(len(rules)))

# Confidence Level = 50%
rules = association_rules(frequent_itemSets, metric='confidence', min_threshold=0.05)
getCountList.append(len(rules))
print("Rules generated at 50% Confidence:  " + str(len(rules)))

# Confidence Level = 40%
rules = association_rules(frequent_itemSets, metric='confidence', min_threshold=0.04)
getCountList.append(len(rules))
print("Rules generated at 40% Confidence:  " + str(len(rules)))

# Confidence Level = 30%
rules = association_rules(frequent_itemSets, metric='confidence', min_threshold=0.03)
getCountList.append(len(rules))
print("Rules generated at 30% Confidence:  " + str(len(rules)))

# Confidence Level = 20%
rules = association_rules(frequent_itemSets, metric='confidence', min_threshold=0.02)
getCountList.append(len(rules))
print("Rules generated at 20% Confidence:  " + str(len(rules)))

# Confidence Level = 10%
rules = association_rules(frequent_itemSets, metric='confidence', min_threshold=0.01)
getCountList.append(len(rules))
print("Rules generated at 10% Confidence:  " + str(len(rules)))


"""
---------------------------------------------------------------------------------------
Question 5:  Rules are generated with a support level of 1%.
---------------------------------------------------------------------------------------
"""
frequent_itemSets = apriori(df2, min_support=0.005, use_colnames=True)

# Confidence Level = 90%
rules = association_rules(frequent_itemSets, metric='confidence', min_threshold=0.09)
getCountList.append(len(rules))
print("Rules generated at 90% Confidence:  " + str(len(rules)))

# Confidence Level = 80%
rules = association_rules(frequent_itemSets, metric='confidence', min_threshold=0.08)
getCountList.append(len(rules))
print("Rules generated at 80% Confidence:  " + str(len(rules)))

# Confidence Level = 70%
rules = association_rules(frequent_itemSets, metric='confidence', min_threshold=0.07)
getCountList.append(len(rules))
print("Rules generated at 70% Confidence:  " + str(len(rules)))

# Confidence Level = 60%
rules = association_rules(frequent_itemSets, metric='confidence', min_threshold=0.06)
getCountList.append(len(rules))
print("Rules generated at 60% Confidence:  " + str(len(rules)))

# Confidence Level = 50%
rules = association_rules(frequent_itemSets, metric='confidence', min_threshold=0.05)
getCountList.append(len(rules))
print("Rules generated at 50% Confidence:  " + str(len(rules)))

# Confidence Level = 40%
rules = association_rules(frequent_itemSets, metric='confidence', min_threshold=0.04)
getCountList.append(len(rules))
print("Rules generated at 40% Confidence:  " + str(len(rules)))

# Confidence Level = 30%
rules = association_rules(frequent_itemSets, metric='confidence', min_threshold=0.03)
getCountList.append(len(rules))
print("Rules generated at 30% Confidence:  " + str(len(rules)))

# Confidence Level = 20%
rules = association_rules(frequent_itemSets, metric='confidence', min_threshold=0.02)
getCountList.append(len(rules))
print("Rules generated at 20% Confidence:  " + str(len(rules)))

# Confidence Level = 10%
rules = association_rules(frequent_itemSets, metric='confidence', min_threshold=0.01)
getCountList.append(len(rules))
print("Rules generated at 10% Confidence:  " + str(len(rules)))


"""
---------------------------------------------------------------------------------------
Question 6:  Rules are generated with a support level of 0.5%.
---------------------------------------------------------------------------------------
"""
frequent_itemSets = apriori(df2, min_support=0.001, use_colnames=True)

# Confidence Level = 90%
rules = association_rules(frequent_itemSets, metric='confidence', min_threshold=0.09)
getCountList.append(len(rules))

print("Rules generated at 90% Confidence:  " + str(len(rules)))

# Confidence Level = 80%
rules = association_rules(frequent_itemSets, metric='confidence', min_threshold=0.08)
getCountList.append(len(rules))
print("Rules generated at 80% Confidence:  " + str(len(rules)))

# Confidence Level = 70%
rules = association_rules(frequent_itemSets, metric='confidence', min_threshold=0.07)
getCountList.append(len(rules))
print("Rules generated at 70% Confidence:  " + str(len(rules)))

# Confidence Level = 60%
rules = association_rules(frequent_itemSets, metric='confidence', min_threshold=0.06)
getCountList.append(len(rules))
print("Rules generated at 60% Confidence:  " + str(len(rules)))

# Confidence Level = 50%
rules = association_rules(frequent_itemSets, metric='confidence', min_threshold=0.05)
getCountList.append(len(rules))
print("Rules generated at 50% Confidence:  " + str(len(rules)))

# Confidence Level = 40%
rules = association_rules(frequent_itemSets, metric='confidence', min_threshold=0.04)
getCountList.append(len(rules))
print("Rules generated at 40% Confidence:  " + str(len(rules)))

# Confidence Level = 30%
rules = association_rules(frequent_itemSets, metric='confidence', min_threshold=0.03)
getCountList.append(len(rules))
print("Rules generated at 30% Confidence:  " + str(len(rules)))

# Confidence Level = 20%
rules = association_rules(frequent_itemSets, metric='confidence', min_threshold=0.02)
getCountList.append(len(rules))
print("Rules generated at 20% Confidence:  " + str(len(rules)))

# Confidence Level = 10%
rules = association_rules(frequent_itemSets, metric='confidence', min_threshold=0.01)
getCountList.append(len(rules))
print("Rules generated at 10% Confidence:  " + str(len(rules)))


"""
---------------------------------------------------------------------------------------
Question 7:  Results of questions 4, 5, 6 and choose the optimal threshold value for 
             support and confidence.
---------------------------------------------------------------------------------------
"""

frequent_itemSets = apriori(df2, min_support=0.0005, use_colnames=True)

# Confidence Level = 90%
rules = association_rules(frequent_itemSets, metric='confidence', min_threshold=0.09)
getCountList.append(len(rules))

print("Rules generated at 90% Confidence:  " + str(len(rules)))

# Confidence Level = 80%
rules = association_rules(frequent_itemSets, metric='confidence', min_threshold=0.08)
getCountList.append(len(rules))
print("Rules generated at 80% Confidence:  " + str(len(rules)))

# Confidence Level = 70%
rules = association_rules(frequent_itemSets, metric='confidence', min_threshold=0.07)
getCountList.append(len(rules))
print("Rules generated at 70% Confidence:  " + str(len(rules)))

# Confidence Level = 60%
rules = association_rules(frequent_itemSets, metric='confidence', min_threshold=0.06)
getCountList.append(len(rules))
print("Rules generated at 60% Confidence:  " + str(len(rules)))

# Confidence Level = 50%
rules = association_rules(frequent_itemSets, metric='confidence', min_threshold=0.05)
getCountList.append(len(rules))
print("Rules generated at 50% Confidence:  " + str(len(rules)))

# Confidence Level = 40%
rules = association_rules(frequent_itemSets, metric='confidence', min_threshold=0.04)
getCountList.append(len(rules))
print("Rules generated at 40% Confidence:  " + str(len(rules)))

# Confidence Level = 30%
rules = association_rules(frequent_itemSets, metric='confidence', min_threshold=0.03)
getCountList.append(len(rules))
print("Rules generated at 30% Confidence:  " + str(len(rules)))

# Confidence Level = 20%
rules = association_rules(frequent_itemSets, metric='confidence', min_threshold=0.02)
getCountList.append(len(rules))
print("Rules generated at 20% Confidence:  " + str(len(rules)))

# Confidence Level = 10%
rules = association_rules(frequent_itemSets, metric='confidence', min_threshold=0.01)
getCountList.append(len(rules))
print("Rules generated at 10% Confidence:  " + str(len(rules)))

height = [10, 24, 36, 40, 5]
tick_label = ['90%', '80%', '70%', '60%', '50%', '40%', '30%', '20%', '10%']
fig = plt.figure(figsize=(10, 5))

plt.bar(tick_label, getCountList, color='blue', width=0.4)
plt.xlabel('Confidence Level')
plt.ylabel('Generated Rules')
plt.title('With Support Level 0.5%')

plt.show()
