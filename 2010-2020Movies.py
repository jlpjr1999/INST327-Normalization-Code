#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib as plt
import numpy as np
import datetime


# In[2]:


np.random.seed(0)


# In[3]:


path = 'csv_data_files/'


# In[4]:


main_df = pd.read_csv("imdb_top_1000.csv")
main_df.info()


# In[5]:


def reduce(x):
    values = x.split()
    return values[0]


# In[6]:


print(reduce("100 mins"))


# In[7]:


main_df["Runtime"] = main_df["Runtime"].apply(reduce)
main_df["Runtime"] = pd.to_numeric(main_df["Runtime"])
main_df["Runtime"]


# In[8]:


val = main_df.iloc[0]["Gross"]
val_t = val.split(",")
new = "".join(val_t)
new


# In[9]:


def remove_commas(x):
    try:
        val_t = x.split(",")
        new = "".join(val_t)
        return new
    except AttributeError:
        return


# In[10]:


remove_commas(np.nan)


# In[11]:


np.nan


# In[12]:


main_df["Gross"]


# In[13]:


main_df["Gross"] = main_df["Gross"].apply(remove_commas)


# In[14]:


main_df["Gross"] = pd.to_numeric(main_df["Gross"], downcast="float")
main_df.info()


# In[15]:


main_df = main_df[main_df["Released_Year"] >= 2010]
main_df.info()


# In[16]:


main_df.mean(axis=0)


# In[17]:


main_df['Meta_score'] = main_df['Meta_score'].apply(lambda x: x if pd.notnull(x) else np.random.randint(main_df['Meta_score'].min(), main_df['Meta_score'].max()))


# In[18]:


main_df.fillna(103720361.3, inplace = True)


# In[19]:


#main_df['Gross'] = main_df['Gross'].apply(lambda x: x if pd.notnull(x) else np.random.randint(main_df['Gross'].min(), main_df['Gross'].max()))


# In[20]:


main_df


# In[21]:


main_df.insert(0, "movie_id", range(1, 1+len(main_df)))


# In[22]:


main_df = main_df.reset_index(drop=True)


# In[23]:


main_df


# In[24]:


main_df.to_csv(path + "imdb_top_248.csv", index=False)


# In[ ]:





# In[ ]:





# In[ ]:





# In[25]:


movies_df = pd.DataFrame({"movie_title" : main_df["Series_Title"]})


# In[26]:


movies_df.info()


# In[27]:


movies_df["production_cost"],movies_df["estimated_income"],movies_df["time_in_theaters_start"],movies_df["time_in_theaters_end"],movies_df["runtime"] = [np.nan, main_df["Gross"], np.nan, np.nan, main_df["Runtime"]]


# In[28]:


movies_df.insert(0, "movie_id", main_df["movie_id"])


# In[29]:


movies_df.info()


# In[30]:


movies_df = movies_df.reset_index(drop=True)


# In[31]:


movies_df


# In[32]:


movies_df['production_cost'] = movies_df['production_cost'].apply(lambda x: x if pd.notnull(x) else np.random.randint(movies_df['estimated_income'].min(), movies_df['estimated_income'].max()))
movies_df["production_cost"] = pd.to_numeric(movies_df["production_cost"], downcast="float")


# In[33]:


movies_df


# In[34]:


movies_df.info()


# In[35]:


def random_date(year):
    month = np.random.randint(1,12)
    day = 0
    if month == 2:
        day = np.random.randint(1,28)
    elif month in (1,3,5,7,8,10,12):
        day = np.random.randint(1,31)
    else:
        day = np.random.randint(1,30)
    return datetime.datetime(year, month, day)


# In[36]:


movies_df['time_in_theaters_start'] = main_df['Released_Year'].apply(random_date).reset_index(drop=True)


# In[37]:


movies_df


# In[38]:


movies_df["time_in_theaters_end"] = movies_df['time_in_theaters_start'].apply(lambda x: x + datetime.timedelta(weeks=np.random.randint(1,4))).reset_index(drop=True)


# In[39]:


movies_df


# In[40]:


movies_df.info()


# In[41]:


movies_df.to_csv(path + "movies.csv", index=False)


# In[ ]:





# In[ ]:





# In[42]:


data = set()
for star in main_df["Star1"]:
    data.add(star)
for star in main_df["Star2"]:
    data.add(star)
for star in main_df["Star3"]:
    data.add(star)
for star in main_df["Star4"]:
    data.add(star)


# In[43]:


data


# In[44]:


data2 = list(data)


# In[45]:


data2


# In[46]:


data2.sort()


# In[47]:


data2


# In[48]:


fnames = []
lnames = []


# In[49]:


for name in data2:
    name_t = name.split(" ", 1)
    if len(name_t) == 1:
        name_t.append("NULL")
    print(name_t)
    fnames.append(name_t[0])
    lnames.append(name_t[1])


# In[50]:


d = {"actor_id": range(1, len(data2)+1), "fname" : fnames, "lname" : lnames}
people_df = pd.DataFrame(d)


# In[51]:


people_df


# In[52]:


people_df.to_csv(path + "people.csv", index=False)


# In[ ]:





# In[ ]:





# In[ ]:





# In[53]:


all_genres = set()
for data in main_df["Genre"]:
    genres = data.split(",")
    for genre in genres:
        all_genres.add(genre.strip())


# In[54]:


all_genres


# In[55]:


all_genres2 = list(all_genres)


# In[56]:


all_genres2.sort()


# In[57]:


d = {"genre_id": range(1, len(all_genres2)+1), "genre" : all_genres2}
genre_df = pd.DataFrame(d)


# In[58]:


genre_df


# In[59]:


genre_df.to_csv(path + "genres.csv", index=False)


# In[ ]:





# In[ ]:





# In[ ]:





# In[60]:


range(1, len(movies_df)+1)


# In[61]:


len(movies_df)


# In[62]:


len(main_df)


# In[63]:


len(movies_df['movie_id'])


# In[64]:


d = {"rating_id": range(1, len(movies_df)+1), "movie_id" : movies_df['movie_id'], "rating" : main_df["Meta_score"]}
rating_df = pd.DataFrame(d)


# In[65]:


rating_df


# In[66]:


rating_df.to_csv(path + "ratings.csv", index=False)


# In[ ]:





# In[ ]:





# In[67]:


genre_to_num = []


# In[68]:


for data in main_df["Genre"]:
    movie_genre_list = []
    genres = data.split(",")
    for genre in genres:
        genre = genre.strip()
        for row_num, listing in genre_df.iterrows():
            if genre == listing['genre']:
                movie_genre_list.append(listing['genre_id'])
    genre_to_num.append(movie_genre_list)


# In[69]:


genre_to_num


# In[70]:


len(genre_to_num)


# In[71]:


movie_id = []
genre_id = []
for row_index, row in movies_df.iterrows():
    for genre in genre_to_num[row_index]:
        movie_id.append(row['movie_id'])
        genre_id.append(genre)


# In[72]:


movie_id


# In[73]:


genre_id


# In[74]:


movie_genre_df = pd.DataFrame({"movie_id" : movie_id, "genre_id" : genre_id})


# In[75]:


movie_genre_df


# In[76]:


movie_genre_df.to_csv(path + "movie_genre.csv", index=False)


# In[ ]:





# In[ ]:





# In[77]:


eth_df = pd.read_csv(path + 'ethnicities_table, sample data.csv')
pronouns_df = pd.read_csv(path + 'pronouns_table, sample data.csv')
roles_df = pd.read_csv(path + 'roles_table, sample data.csv')


# In[78]:


eth_df


# In[79]:


roles_df


# In[80]:


pronouns_df


# In[81]:


actor_ids = []
pronoun_ids = []


# In[82]:


for row_num, actor in people_df.iterrows():
    num_pronouns = np.random.randint(1,4)
    i=0
    while i < num_pronouns:
        pronoun = np.random.randint(1,15)        
        actor_ids.append(actor['actor_id'])
        pronoun_ids.append(pronoun)
        i +=1


# In[83]:


actor_ids


# In[84]:


len(actor_ids)


# In[85]:


pronoun_ids


# In[86]:


len(pronoun_ids)


# In[87]:


people_pronouns_df = pd.DataFrame({"actor_id": actor_ids, "pronoun_id": pronoun_ids})


# In[88]:


people_pronouns_df


# In[89]:


people_pronouns_df.to_csv(path + "people_pronouns.csv", index=False)


# In[ ]:





# In[ ]:





# In[ ]:





# In[90]:


actor_ids = []
ethnicities_id = []


# In[91]:


for row_num, actor in people_df.iterrows():
    num_ethnicities = np.random.randint(1,4)
    i=0
    while i < num_ethnicities:
        ethn = np.random.randint(1,21)
        actor_ids.append(actor['actor_id'])
        ethnicities_id.append(ethn)
        i +=1


# In[92]:


actor_ids


# In[93]:


ethnicities_id


# In[94]:


people_eth_df = pd.DataFrame({"actor_id": actor_ids, "ethnicity_id": ethnicities_id})


# In[95]:


people_eth_df


# In[96]:


people_eth_df.to_csv(path + "people_ethnicities.csv", index=False)


# In[ ]:





# In[ ]:





# In[ ]:





# In[97]:


actor_ids = []
movie_id = []
role_id = []
pay = []


# In[98]:


for row_num, movie in main_df.iterrows():
    for row_num, actor in people_df.iterrows():
        actor_name = ""
        if actor['lname'] == "NULL":
            actor_name = actor['fname']
        else:
            actor_name = actor['fname'] + " " + actor['lname']
        actor_name = actor_name.strip()
        if movie['Star1'] == actor_name:
            actor_ids.append(actor['actor_id'])
            movie_id.append(movie['movie_id'])
            role_id.append(np.random.randint(1,6))
        if movie['Star2'] == actor_name:
            actor_ids.append(actor['actor_id'])
            movie_id.append(movie['movie_id'])
            role_id.append(np.random.randint(1,6))
        if movie['Star3'] == actor_name:
            actor_ids.append(actor['actor_id'])
            movie_id.append(movie['movie_id'])
            role_id.append(np.random.randint(1,6))
        if movie['Star4'] == actor_name:
            actor_ids.append(actor['actor_id'])
            movie_id.append(movie['movie_id'])
            role_id.append(np.random.randint(1,6))


# In[99]:


for i in range(1, len(actor_ids)+1):
    pay.append(np.random.randint(30000,410000))


# In[100]:


len(actor_ids)


# In[101]:


actor_ids


# In[102]:


len(movie_id)


# In[103]:


movie_id


# In[104]:


len(role_id)


# In[105]:


role_id


# In[106]:


len(pay)


# In[107]:


print(pay)


# In[108]:


casting_roles_df = pd.DataFrame({"actor_id": actor_ids, "movie_id": movie_id, "role_id": role_id, "pay": pay})


# In[109]:


casting_roles_df.head(12)


# In[110]:


casting_roles_df.to_csv(path + "casting_roles.csv", index=False)

