
from .models import User, Emprendimiento
import re
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from operator import itemgetter


def apriori(id):
    # Data Preprocessing
    user_id = id.data['user_id']
    qs = User.objects.all().values_list('liked')
    app_names_list = list(val[0] for val in qs)

    userQs = User.objects.filter(user_id=user_id).values('liked')[0]['liked']
    userStr =  re.sub("\[|\'|\]","",userQs)
    userLikedList = userStr.split(sep=',')
    recommendedValue = userLikedList

    transactions = []
    for emp in range(0, len(app_names_list)):
        string = re.sub("\"|\[|\'|\]","",app_names_list[emp])
        newString = string.split(sep=',')
        transactions.append(newString)
    
    # Training the Apriori model on the dataset
    from apyori import apriori
    rules = apriori(transactions = transactions, min_support = 0.02, min_confidence = 0.2, min_lift = 3, min_length = 2, max_length = 2)

    ## Displaying the first results coming directly from the output of the apriori function
    results = list(rules)
    results

    ## Putting the results well organised into a list
    def inspect(results):
        lhs         = [tuple(result[2][0][0])[0] for result in results]
        rhs         = [tuple(result[2][0][1])[0] for result in results]
        supports    = [result[1] for result in results]
        confidences = [result[2][0][2] for result in results]
        lifts       = [result[2][0][3] for result in results]
        return list(zip(lhs, rhs, supports, confidences, lifts))

    resultsinApriory = inspect(results)
    resultsinApriory = list(list(val) for val in resultsinApriory)
    
    #Order rules by lift
    resultsinApriorySorted = sorted(resultsinApriory, key=itemgetter(4), reverse=True)

    unique_recommendedValue = []
    [unique_recommendedValue.append(recomValue.strip()) for recomValue in recommendedValue if recomValue.strip() not in unique_recommendedValue]

    userRules = []
    for recomValue in range(0, len(unique_recommendedValue)):
        userRules = [rule[0].strip() for rule in resultsinApriorySorted if unique_recommendedValue[recomValue] in rule[1].strip()]

    unique_userRules = []
    [unique_userRules.append(rule) for rule in userRules if rule not in unique_userRules]

    result = []
    for rule in range(0,5):
        print(unique_userRules[rule].strip())
        result.append(Emprendimiento.objects.filter(type=unique_userRules[rule].strip()).values()[:1][0])

    return result



