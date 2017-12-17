import sqlite3
import sys
import random

SQL=r'''SELECT trainSearchStream.*,
       SearchInfo.IPID,
       SearchInfo.IsUserLoggedOn,
       SearchInfo.SearchDate,
       SearchInfo.SearchParams,
       SearchInfo.SearchQuery,
       UserInfo.*,
       AdsInfo.Params,
       AdsInfo.Price,
       AdsInfo.Title,
       SearchLocation.LocationID AS SearchLocationID,
       SearchLocation.Level AS SearchLocationLevel,
       SearchLocation.RegionID AS SearchRegionID,
       SearchLocation.CityID AS SearchCityID,
       AdsLocation.LocationID AS AdsLocationID,
       AdsLocation.Level AS AdsLocationLevel,
       AdsLocation.RegionID AS AdsRegionID,
       AdsLocation.CityID AS AdsCityID,
       SearchCategory.CategoryID AS SearchCategoryID,
       SearchCategory.Level AS SearchCategoryLevel,
       SearchCategory.ParentCategoryID AS SearchParentCategoryID,
       SearchCategory.SubcategoryID AS SearchSubcategoryID,
       AdsCategory.CategoryID AS AdsCategoryID,
       AdsCategory.Level AS AdsCategoryLevel,
       AdsCategory.ParentCategoryID AS AdsParentCategoryID,
       AdsCategory.SubcategoryID AS AdsSubcategoryID
  FROM trainSearchStream
       LEFT JOIN
       SearchInfo ON trainSearchStream.SearchID = SearchInfo.SearchID
       LEFT JOIN
       UserInfo ON SearchInfo.UserID = UserInfo.UserID
       LEFT JOIN
       AdsInfo ON AdsInfo.AdID = trainSearchStream.AdID
       LEFT JOIN
       Location AS SearchLocation ON SearchLocation.LocationID = SearchInfo.LocationID
       LEFT JOIN
       Location AS AdsLocation ON AdsLocation.LocationID = AdsInfo.LocationID
       LEFT JOIN
       Category AS SearchCategory ON SearchCategory.CategoryID = SearchInfo.CategoryID
       LEFT JOIN
       Category AS AdsCategory ON AdsCategory.CategoryID = AdsInfo.CategoryID
WHERE AdsInfo.AdID=?;
'''

if __name__=='__main__':
    conn=sqlite3.connect(sys.argv[1])
    result_num=int(sys.argv[2])
    cursor=conn.cursor()
    count = cursor.execute(r'SELECT MAX(_ROWID_) FROM AdsInfo LIMIT 1;').fetchone()
    print (count)

    choices = random.sample(range(count[0]),result_num)
    result = [print(i) or cursor.execute(SQL,(i,)).fetchall() for i in choices]
    print (result)
