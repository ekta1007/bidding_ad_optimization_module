#SchemaDesign.py

#Running the sql bath file from mysql CLI
SHOW FULL PROCESSLIST
tee D:\Desktop\logfile.txt
source D:\Desktop\script1_PROJECT_NAME.sql
notee # close the logfile.txt



use ad_bidding_1 ;

drop table if exists tab_1 ;
create table tab_1
(DT LONGTEXT   ,AUCTION_ID_64 BIGINT  UNSIGNED ,USER_ID_64 BIGINT  UNSIGNED ,TAG_ID INT  UNSIGNED,INVENTORY_SOURCE_ID MEDIUMINT UNSIGNED ,INVENTORY_CLASS SMALLINT ,SITE_DOMAIN LONGTEXT ,WIDTH SMALLINT UNSIGNED,HEIGHT SMALLINT UNSIGNED ,GEO_COUNTRY VARCHAR(300) ,GEO_REGION VARCHAR(300) ,GENDER VARCHAR(300) ,AGE SMALLINT UNSIGNED ,SELLER_MEMBER_ID BIGINT  UNSIGNED ,BUYER_MEMBER_ID SMALLINT  UNSIGNED ,CREATIVE_ID BIGINT  UNSIGNED ,BUYER_CURRENCY VARCHAR(300) ,BUYER_BID LONGTEXT ,BUYER_SPEND LONGTEXT ,ECP LONGTEXT ,RESERVE_PRICE LONGTEXT ,ADVERTISER_ID BIGINT  UNSIGNED  ,CAMPAIGN_GROUP_ID BIGINT  UNSIGNED ,CAMPAIGN_ID  BIGINT  UNSIGNED ,CREATIVE_FREQ  SMALLINT  UNSIGNED ,CREATIVE_REC  SMALLINT  UNSIGNED ,IS_LEARN  SMALLINT  UNSIGNED,IS_REMARKETING  SMALLINT  UNSIGNED ,ADVERTISER_FREQUENCY  SMALLINT  UNSIGNED,ADVERTISER_RECENCY SMALLINT UNSIGNED ,USER_GROUP_ID SMALLINT  UNSIGNED ,CAMP_DP_ID LONGTEXT ,MEDIA_BUY_ID BIGINT  UNSIGNED ,MEDIA_BUY_COST LONGTEXT ,BRAND_ID LONGTEXT ,CLEARED_DIRECT LONGTEXT ,CLEAR_FEES LONGTEXT ,BOOKED_REVENUE LONGTEXT ,CAN_CONVERT LONGTEXT ,IS_CONTROL LONGTEXT ,ACTUAL_BID LONGTEXT ,PIXEL_ID LONGTEXT ,SITE_ID LONGTEXT ,AUCTION_SERVICE_FEES LONGTEXT ,DISCREPANCY_ALLOWANCE LONGTEXT ,CREATIVE_OVERAGE_FEES LONGTEXT ,FOLD_POSITION SMALLINT ,CADENCE_MODIFIER LONGTEXT ,IMP_TYPE SMALLINT ,IP_ADDRESS LONGTEXT ,ORDER_ID LONGTEXT ,EXTERNAL_DATA LONGTEXT ,PUBLISHER_ID BIGINT  UNSIGNED ,AUCTION_SERVICE_DEDUCTION LONGTEXT ,EVENT_TYPE VARCHAR(300)  ) ;


LOAD DATA LOCAL INFILE 
'D:\\Desktop\\Downloads\\PROJECT_NAME\\Unzipped_files\\0013c0b1-ef2a-4d23-ae41-6267a3035288_000000'
INTO TABLE tab_1 
FIELDS TERMINATED BY '\t' 
LINES TERMINATED BY '\n'
(DT,AUCTION_ID_64,USER_ID_64,TAG_ID,INVENTORY_SOURCE_ID,INVENTORY_CLASS,SITE_DOMAIN,WIDTH,HEIGHT,GEO_COUNTRY,GEO_REGION,GENDER,AGE,SELLER_MEMBER_ID,BUYER_MEMBER_ID,CREATIVE_ID,BUYER_CURRENCY,BUYER_BID,BUYER_SPEND,ECP,RESERVE_PRICE,ADVERTISER_ID,CAMPAIGN_GROUP_ID,CAMPAIGN_ID,CREATIVE_FREQ,CREATIVE_REC,IS_LEARN,IS_REMARKETING,ADVERTISER_FREQUENCY,ADVERTISER_RECENCY,USER_GROUP_ID,CAMP_DP_ID,MEDIA_BUY_ID,MEDIA_BUY_COST,BRAND_ID,CLEARED_DIRECT,CLEAR_FEES,BOOKED_REVENUE,CAN_CONVERT,IS_CONTROL,ACTUAL_BID,PIXEL_ID,SITE_ID,AUCTION_SERVICE_FEES,DISCREPANCY_ALLOWANCE,CREATIVE_OVERAGE_FEES,FOLD_POSITION,CADENCE_MODIFIER,IMP_TYPE,IP_ADDRESS,ORDER_ID,EXTERNAL_DATA,PUBLISHER_ID,AUCTION_SERVICE_DEDUCTION,EVENT_TYPE);

select * from tab_1
limit 10;

# Testing import of schema signature by record counts 
num_lines=[]
num_lines.append(sum(1 for line in open('D:/Desktop/Downloads/PROJECT_NAME/Unzipped_files/0013c0b1-ef2a-4d23-ae41-6267a3035288_000000')))
num_lines.append(sum(1 for line in open('D:/Desktop/Downloads/PROJECT_NAME/Unzipped_files/0013c0b1-ef2a-4d23-ae41-6267a3035288_000001')))
num_lines.append(sum(1 for line in open('D:/Desktop/Downloads/PROJECT_NAME/Unzipped_files/0013c0b1-ef2a-4d23-ae41-6267a3035288_000002')))
num_lines.append(sum(1 for line in open('D:/Desktop/Downloads/PROJECT_NAME/Unzipped_files/cd7a58dc-2053-4811-8463-b144781352ac_000000')))
num_lines.append(sum(1 for line in open('D:/Desktop/Downloads/PROJECT_NAME/Unzipped_files/cd7a58dc-2053-4811-8463-b144781352ac_000001')))
num_lines.append(sum(1 for line in open('D:/Desktop/Downloads/PROJECT_NAME/Unzipped_files/cd7a58dc-2053-4811-8463-b144781352ac_000002')))
num_lines.append(sum(1 for line in open('D:/Desktop/Downloads/PROJECT_NAME/Unzipped_files/cd7a58dc-2053-4811-8463-b144781352ac_000003')))
num_lines.append(sum(1 for line in open('D:/Desktop/Downloads/PROJECT_NAME/Unzipped_files/cd7a58dc-2053-4811-8463-b144781352ac_000004')))
num_lines.append(sum(1 for line in open('D:/Desktop/Downloads/PROJECT_NAME/Unzipped_files/cd7a58dc-2053-4811-8463-b144781352ac_000005')))
num_lines.append(sum(1 for line in open('D:/Desktop/Downloads/PROJECT_NAME/Unzipped_files/cd7a58dc-2053-4811-8463-b144781352ac_000006')))
#num_lines will have the list of all records, per individual file 

# Now creating merge based on primary key
