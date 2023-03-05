import mysql.connector
import csv
csv.field_size_limit(100000000)

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="test"
)

# Creating an instance of 'cursor' class
# which is used to execute the 'SQL'
# statements in 'Python'
cursor = mydb.cursor()


# Open file
# i = 0
with open('domains_export.csv', "r", errors='ignore') as file_obj:

    reader_obj = csv.reader(file_obj)

    for i, row in enumerate(reader_obj):
        # if i < 3800000:
        #     print(i)
        #     continue

        # try:
        sql = """INSERT INTO new_domains (
            domain,
            alexa_rank,
            aliases,
            alternates,
            android_app_id,
            average_product_price,
            brands_page_url,
            categories,
            city,
            collections,
            combined_followers,
            common_crawl_centrality,
            common_crawl_pagerank,
            company_ids,
            company_location,
            contact_page_url,
            country_code,
            created,
            currency,
            description,
            domain_tld1,
            domain_url,
            emails,
            employee_count,
            estimated_monthly_sales,
            facebook,
            facebook_categories,
            facebook_followers,
            facebook_followers_30d,
            facebook_followers_90d,
            facebook_group,
            facebook_group_followers,
            facebook_group_followers_30d,
            facebook_group_followers_90d,
            facebook_group_url,
            facebook_url,
            favicon_url,
            features,
            financing_page_url,
            instagram,
            instagram_categories,
            instagram_followers,
            instagram_followers_30d,
            instagram_followers_90d,
            instagram_posts,
            instagram_url,
            installed_apps,
            ios_app_id,
            language_code,
            last_plan,
            last_plan_changed,
            last_platform,
            last_platform_changed,
            linkedin_account,
            linkedin_url,
            maximum_product_price,
            merchant_name,
            meta_description,
            meta_keywords,
            minimum_product_price,
            monthly_app_spend,
            most_recent_product_image_url,
            most_recent_product_title,
            most_recent_product_url,
            open_graph_image_url,
            phones,
            pinterest,
            pinterest_followers,
            pinterest_followers_30d,
            pinterest_followers_90d,
            pinterest_posts,
            pinterest_url,
            plan,
            platform,
            platform_domain,
            platform_rank,
            product_images,
            product_images_created_30,
            product_images_created_365,
            product_images_created_90,
            product_variants,
            products_sold,
            rank,
            region,
            retailer_url,
            returns_page_url,
            sales_channels,
            shipping_carriers,
            state,
            status,
            street_address,
            subregion,
            tags,
            technologies,
            theme,
            theme_spend,
            theme_vendor,
            tiktok,
            tiktok_followers,
            tiktok_followers_30d,
            tiktok_followers_90d,
            tiktok_url,
            title,
            tracking_page_url,
            twitter,
            twitter_followers,
            twitter_followers_30d,
            twitter_followers_90d,
            twitter_posts,
            twitter_url,
            vendor_count,
            warranty_page_url,
            youtube,
            youtube_followers,
            youtube_followers_30d,
            youtube_followers_90d,
            youtube_url,
            zip,
            store_locator_url,
            est_dollars
) VALUES(
            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
            )
            """
        try:
            est_dollars = row[24].replace('USD $', '').replace(',', '')
            est_dollars = int(float(est_dollars))
        except Exception:
            est_dollars = 0
        val = ('row[0]', 'row[1]', 'row[2]', 'row[3]', 'row[4]', 'row[5]', 'row[6]', 'row[7]', 'row[8]', 'row[9]', 'row[10]', 'row[11]', 'row[12]', 'row[13]', 'row[14]', 'row[15]', 'row[16]', 'row[17]', 'row[18]', 'row[19]', 'row[20]', 'row[21]', 'row[22]', 'row[23]', 'row[24]', 'row[25]', 'row[26]', 'row[27]', 'row[28]', 'row[29]', 'row[30]', 'row[31]', 'row[32]', 'row[33]', 'row[34]', 'row[35]', 'row[36]', 'row[37]', 'row[38]', 'row[39]', 'row[40]', 'row[41]', 'row[42]', 'row[43]', 'row[44]', 'row[45]', 'row[46]', 'row[47]', 'row[48]', 'row[49]', 'row[50]', 'row[51]', 'row[52]', 'row[53]', 'row[54]', 'row[55]', 'row[56]', 'row[57]', 'row[58]', 'row[59]', 'row[60]', 'row[61]', 'row[62]', 'row[63]', 'row[64]', 'row[65]', 'row[66]', 'row[67]', 'row[68]', 'row[69]', 'row[70]', 'row[71]', 'row[72]', 'row[73]', 'row[74]', 'row[75]', 'row[76]', 'row[77]', 'row[78]', 'row[79]', 'row[80]', 'row[81]', 'row[82]', 'row[83]', 'row[84]', 'row[85]', 'row[86]', 'row[87]', 'row[88]', 'row[89]', 'row[90]', 'row[91]', 'row[92]', 'row[93]', 'row[94]', 'row[95]', 'row[96]', 'row[97]', 'row[98]', 'row[99]', 'row[100]', 'row[101]', 'row[102]', 'row[103]', 'row[104]', 'row[105]', 'row[106]', 'row[107]', 'row[108]', 'row[109]', 'row[110]', 'row[111]', 'row[112]', 'row[113]', 'row[114]', 'row[115]', 'row[116]', 'row[117]', 'row[118]', est_dollars)
        cursor.execute(sql, val)
        print(i)
        # if i == 3840533:
        #     break
        # except Exception as e:
        #     print(e)
mydb.commit()
# Create reader object by passing the file
# object to reader method
# reader_obj = csv.reader(file_obj)

# Iterate over each row in the csv
# file using reader object
# for row in reader_obj:
#     print(row)


# with open('domains_export (1).csv') as file_obj:
