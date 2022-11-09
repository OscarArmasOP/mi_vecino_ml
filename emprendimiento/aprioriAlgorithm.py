
from .models import Emprendimiento, User
from operator import itemgetter
from apyori import apriori

def aprioriFunction(user_id):
    # Data Preprocessing for user 
    user_id = user_id
    print('Step3')
    user_categoriesQS = User.objects.filter(user_id=user_id).values_list('emprendimientos_categories')[0][0]
    favorite_empQS = User.objects.filter(user_id=user_id).values_list('favorite_emprendimientos')[0][0]
    user_categories = []
    print('Step4')
    if(user_categoriesQS is not None):
        user_categories = list(val.get('name') for val in user_categoriesQS)
        # favorite_emp = list(val.get('name') for val in favorite_empQS)
        # user_categories.append(favorite_emp)
    else:
        user_categories = list(val.get('name') for val in favorite_empQS)
    recommendedValue = user_categories
    # Data Preprocessing for apriori
    usersQS = User.objects.all().values_list('emprendimientos_categories')
    transactions = []
    for category in range(0, len(usersQS)):
        transactions.append(list(val.get('name') for val in usersQS[category][0]))

    # Training the Apriori model on the dataset
    rules = apriori(transactions = transactions, min_support = 0.02, min_confidence = 0.02, min_lift = 2, min_length = 2, max_length = 2)
    ## Displaying the first results coming directly from the output of the apriori function
    results = list(rules)
    results
    print('Step5')
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
    [unique_recommendedValue.append(recomValue) for recomValue in recommendedValue if recomValue not in unique_recommendedValue]

    userRules = []
    for recomValue in range(0, len(unique_recommendedValue)):
        userRules = [rule[0] for rule in resultsinApriorySorted if unique_recommendedValue[recomValue] in rule[1]]
    if(len(userRules) == 0):
        for recomValue in range(0, 5):
            userRules = [rule[0] for rule in resultsinApriorySorted]
    unique_userRules = []
    [unique_userRules.append(rule) for rule in userRules if rule not in unique_userRules]
    result = []
    print('Step6')
    for rule in range(0,1):
        result.append(Emprendimiento.objects.filter(categories__0__type=unique_userRules[rule]).values()[:1][0])
    return result