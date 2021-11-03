from django.db import connection

def clubpositionaverage(year):
    with connection.cursor() as cursor:
        cursor.execute(
            '''
            SELECT club_name[1] AS clubid, club_name[2] AS club_name, club_name[3] AS year, att,mid,def FROM crosstab(
            $$ SELECT ARRAY[DC.clubid, FP.club_name, year]::text[],
            position_category,
            ROUND(AVG(overall)) AS Club_overall
            FROM public."Fact.PlayerStats" AS FP
            LEFT JOIN public."Dim.Positions" AS DP ON FP.positionid = DP.positionid
            LEFT JOIN public."Dim.Positioncategory" AS DPC ON DP.position_categoryid = DPC.position_categoryid
            LEFT JOIN public."Dim.Clubs" AS DC ON FP.club_name = DC.club_name
            LEFT JOIN public."Dim.Leagues" AS DL ON DC.leagueid = DL.leagueid
            GROUP BY DC.clubid, FP.club_name, year, position_category, DL.rank
            HAVING position_category != 'None' AND DL.rank = 1 AND year = '''+ str(year) +'''
            $$, $$ VALUES('ATT'), ('MID'), ('DEF') $$ )
            AS ct(club_name text[], ATT integer, MID integer, DEF integer )

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