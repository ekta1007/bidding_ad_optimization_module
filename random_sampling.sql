set @total=(select count(*) from tab_1 where predict_var ="4" or predict_var ="2" ) ;
set @sample= ( select @total*(70/30))  ;

# select @total,@sample
#@total,@sample
#4090,9543.333331970

# Generic syntax 
PREPARE STMT FROM 'SELECT * FROM tab_1 ORDER BY RAND() LIMIT ?';
EXECUTE STMT USING @sample;

# or if I were to store all the (temp) tables along wth the randomization - Inserted "create table clause here"
PREPARE STMT FROM "CREATE TABLE tab_derived_1 SELECT * FROM tab_1 WHERE predict_var = '4'   or predict_var = '2'  union 
(SELECT * FROM tab_1 WHERE predict_var = '0' or predict_var = '1' ORDER BY RAND() limit ?  )" ;
EXECUTE STMT USING @sample;



PREPARE STMT FROM " SELECT * FROM tab_1 WHERE predict_var = '4' or predict_var = '2'  union 
(SELECT * FROM tab_1 WHERE predict_var = '0' or predict_var = '1' ORDER BY RAND() limit ?  )" ;
EXECUTE STMT USING @sample; # fetches a total of 13,633 records

# vars used
# DT ,AUCTION_ID_64 ,USER_ID_64  ,INVENTORY_SOURCE_ID  , SITE_DOMAIN ,area_custom,GENDER  ,AGE  , SELLER_MEMBER_ID , CREATIVE_ID   ,BUYER_BID  , BUYER_SPEND  , ECP  , RESERVE_PRICE  , CAMPAIGN_GROUP_ID   ,CAMPAIGN_ID  ,CREATIVE_FREQ   ,CREATIVE_REC   ,IS_LEARN   , ADVERTISER_FREQUENCY  , ADVERTISER_RECENCY  ,USER_GROUP_ID  ,MEDIA_BUY_ID  ,MEDIA_BUY_COST ,CLEARED_DIRECT ,BOOKED_REVENUE  ,CAN_CONVERT ,ACTUAL_BID ,PIXEL_ID ,SITE_ID  ,AUCTION_SERVICE_FEES  ,DISCREPANCY_ALLOWANCE ,FOLD_POSITION ,CADENCE_MODIFIER  IMP_TYPE,	PUBLISHER_ID,	AUCTION_SERVICE_DEDUCTION,	EVENT_TYPE,day_week,time_day ,predict_var


