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
    return 0:
    

