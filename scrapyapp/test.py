import MySQLdb
import sys
import nltk
host = "localhost"
user = "root"
password = 'welcome'
database = "my_jobs"
# try:
#     conn = MySQLdb.connect( host, user, password, database, use_unicode=True, charset="utf8")
#     cursor = conn.cursor()
#     query="""INSERT INTO tesing (item_url, title, price, discount) VALUES (%s, %s, %s, %s)"""
#     url = 'uuuuuuuu'
#     title = 'ttttttttt'
#     sku = 'ssssssssss'
#     upc = 'ppppppppp'
#     price = 100
#     discount = 10
#     params=(url, title, price, discount)
#     cursor.execute(query, params)
#     conn.commit()
# except:
#     print sys.exc_info()
#     pass
# finally:
#     conn.close()
# print "Data saved successfully."

abc = [
    {
        "@context":"http://schema.org/",
        "@type":"Product",
        "name":"Fabstone Collection Solid Men's Hooded Blue T-Shirt",
        "image":"https://rukminim1.flixcart.com/image/128/128/jc7z0y80/t-shirt/x/f/f/s-fabstonemensfullbluehoodtshirt-fabstone-original-imaffebntdctjmmu.jpeg?q=70",
        "aggregateRating":{
            "@type":"AggregateRating",
            "ratingValue":3.9,
            "reviewCount":1063
        },
        "brand": {
            "@type":"Thing",
            "name":"Fabstone Collection"
        }
    },
    {
        "@context":"http://schema.org",
        "@type":"BreadcrumbList",
        "itemListElement":[
            {
                "@type":"ListItem",
                "position":1,
                "item":{
                    "@id":"https://www.flipkart.com/?otracker=product_breadCrumbs_Home",
                    "name":"Home"
                    }
            },
            {
                "@type":"ListItem",
                "position":2,
                "item":{
                    "@id":"https://www.flipkart.com/clothing/pr?sid=2oq&marketplace=FLIPKART&otracker=product_breadCrumbs_Clothing",
                    "name":"Clothing"
                }
            },
            {
                "@type":"ListItem",
                "position":3,
                "item":{
                    "@id":"https://www.flipkart.com/mens-clothing/pr?sid=2oq,s9b&marketplace=FLIPKART&otracker=product_breadCrumbs_Men%27s+Clothing",
                    "name":"Men's Clothing"
                    }
            },
            {
                "@type":"ListItem",
                "position":4,
                "item":{
                    "@id":"https://www.flipkart.com/men/tshirts/pr?sid=2oq,s9b,j9y&marketplace=FLIPKART&otracker=product_breadCrumbs_T-Shirts",
                    "name":"T-Shirts"
                }
            },
            {
                "@type":"ListItem",
                "position":5,
                "item":{
                    "@id":"https://www.flipkart.com/men/tshirts/fabstone-collection~brand/pr?sid=2oq,s9b,j9y&marketplace=FLIPKART&otracker=product_breadCrumbs_Fabstone+Collection+T-Shirts",
                    "name":"Fabstone Collection T-Shirts"
                }
            },
            {
                "@type":"ListItem",
                "position":6,
                "item":{
                    "@id":"https://www.flipkart.com/fabstone-collection-solid-men-s-hooded-blue-t-shirt/p/itmf3yum5mvdue8w?otracker=product_breadCrumbs_Fabstone+Collection+Solid+Men%27s+Hooded+Blue+T-Shirt",
                    "name":"Fabstone Collection Solid Men's Hooded Blue T-Shirt"
                }
            }
        ]
    }
]

abc = str(abc)
import json
print 'tttttttt : ',type(abc)
k = json.dumps(abc)
q = json.loads(k)
print type(q)