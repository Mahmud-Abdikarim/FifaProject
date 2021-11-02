from django.db import connection

def clubpositionaverage():
    with connection.cursor() as cursor:
        cursor.execute(
            '''
            SELECT FP.club_name,
            position_category,
            ROUND(AVG(overall)) AS Club_overall
            FROM public."Fact.PlayerStats" AS FP
            LEFT JOIN public."Dim.Positions" AS DP ON FP.positionid = DP.positionid
            LEFT JOIN public."Dim.Positioncategory" AS DPC ON DP.position_categoryid = DPC.position_categoryid
            LEFT JOIN public."Dim.Clubs" AS DC ON FP.club_name = DC.club_name
            LEFT JOIN public."Dim.Leagues" AS DL ON DC.leagueid = DL.leagueid
            GROUP BY FP.club_name, position_category, DL.rank
            HAVING position_category != 'None' AND DL.rank = 1
            '''
        )
            #row = cursor.fetchall()
            #row = list(row[0])
        columns = [col[0] for col in cursor.description]
        fetched = cursor.fetchall()
        row = [
            dict(zip(columns, row))
            for row in fetched
        ]
    
    return row