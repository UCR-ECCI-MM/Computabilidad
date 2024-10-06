from io import BytesIO
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def get_category_frequency(medline_dict):
    """
    This function takes a dictionary `medline_dict` and counts the frequency of information categories
    within health topics. It returns a dictionary with the categories and their respective counts.
    """
    # dictionary used to storage the category counts 
    inf_category_counts = {}
    # verify that the key exists
    if 'health_topics' in medline_dict:
        # verify the value is a list 
        if isinstance(medline_dict['health_topics'], list):
            for topic in medline_dict['health_topics']:
                # verify that topic is a dict and the existence of the key
                if isinstance(topic, dict) and 'tags' in topic:
                    #print("Topic es dic y existe tags")
                    if 'site' in topic['tags']:
                        if isinstance(topic['tags']['site'], list):
                            for site in topic['tags']['site']:
                                if ('tags' in site) and (isinstance(site['tags'], dict)):
                                    if ('information-category' in site['tags']) and (isinstance(site['tags']['information-category'], list)):
                                        for category in site['tags']['information-category']: 
                                            if category in inf_category_counts:
                                            # if the key is in the dict, increase the counter
                                                inf_category_counts[category] += 1
                                            else:
                                                # add the key with initial value of 1
                                                inf_category_counts[category] = 1
                                
    print(inf_category_counts)
    return inf_category_counts


def get_image_frequent_categories(inf_category_counts):
    columns=['Category', 'Count']
    # cast the `inf_category_counts` dictionary to a dataFrame
    df_category_counts = pd.DataFrame(list(inf_category_counts.items()), columns=columns)
    # get the 10 most popular categories
    popular_category_counts = df_category_counts.sort_values(by='Count', ascending=False).head(10)

    # create a horizontal barplot
    plt.figure(figsize=(6, 6))
    sns.barplot(x='Count', y='Category', data=popular_category_counts, orient='h')
    plt.xlabel('Count')
    plt.ylabel('Category')
    plt.tight_layout()
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    plt.close()
    return buffer

