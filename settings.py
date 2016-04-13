# settings.py
def init():
    global number_of_nodes
    global max_time
    global num_trials
    global bite_prob
    global network_type
    global heal_prob
    global innovation_prob
    global imitation_prob
    global timeout
    global outside_effects_prob
    global anger_prob
    global joy_prob
    global sadness_prob
    global disgust_prob
    global tweet_probability_users
    global tweet_relevant_probability
    global tweet_probability_about
    global sentiment_about
    global tweet_probability_enterprises
    global enterprises

    network_type=1
    number_of_nodes=50
    max_time=500
    num_trials=1
    timeout=1

    #Zombie model
    bite_prob=0.01 # 0-1
    heal_prob=0.01 # 0-1

    #Bass model
    innovation_prob=0.001
    imitation_prob=0.005

    #Sentiment Correlation model
    outside_effects_prob = 0.2
    anger_prob = 0.06
    joy_prob = 0.05
    sadness_prob = 0.02
    disgust_prob = 0.02

    #Big Market model
    ##Names
    enterprises = ["BBVA","Santander", "Bankia"]
    ##Users
    tweet_probability_users = 0.44
    tweet_relevant_probability = 0.25
    tweet_probability_about = [0.15, 0.15, 0.15]
    sentiment_about = [0, 0, 0] #Valores por defecto
    ##Enterprises
    tweet_probability_enterprises = [0.3, 0.3, 0.3]

