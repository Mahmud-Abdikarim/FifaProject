# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class DimBodytype(models.Model):
    id = models.IntegerField(primary_key=True)
    body_type = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'Dim.BodyType'


class DimClubs(models.Model):
    clubid = models.BigIntegerField(primary_key=True)
    club_name = models.CharField(max_length=50, blank=True, null=True)
    leagueid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Dim.Clubs'


class DimCountry(models.Model):
    countryid = models.IntegerField(primary_key=True)
    country = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'Dim.Country'


class DimLeagues(models.Model):
    leagueid = models.IntegerField(primary_key=True)
    league = models.CharField(max_length=-1)
    rank = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Dim.Leagues'


class DimPlayers(models.Model):
    sofifa_id = models.IntegerField(primary_key=True)
    short_name = models.CharField(max_length=-1)
    long_name = models.CharField(max_length=-1)
    dob = models.DateField()

    class Meta:
        managed = False
        db_table = 'Dim.Players'


class DimPositioncategory(models.Model):
    position_categoryid = models.IntegerField(blank=True, null=True)
    position_category = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Dim.Positioncategory'


class DimPositions(models.Model):
    position = models.CharField(max_length=50, blank=True, null=True)
    positionid = models.IntegerField(primary_key=True)
    position_categoryid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Dim.Positions'


class DimPreferredfoot(models.Model):
    id = models.IntegerField(primary_key=True)
    preferred_foot = models.CharField(max_length=5)

    class Meta:
        managed = False
        db_table = 'Dim.PreferredFoot'


class DimRealface(models.Model):
    id = models.IntegerField(primary_key=True)
    real_face = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'Dim.RealFace'


class DimWorkrate(models.Model):
    id = models.IntegerField(primary_key=True)
    work_rate = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'Dim.WorkRate'


class FactPlayerpositions(models.Model):
    sofifa_id = models.IntegerField()
    position = models.CharField(max_length=-1)
    year = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Fact.PlayerPositions'


class FactPlayerstats(models.Model):
    id = models.BigIntegerField(blank=True, null=True)
    sofifa_id = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    player_url = models.CharField(max_length=200, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    height_cm = models.IntegerField(blank=True, null=True)
    weight_kg = models.IntegerField(blank=True, null=True)
    nationality = models.CharField(max_length=50, blank=True, null=True)
    club_name = models.CharField(max_length=50, blank=True, null=True)
    league_name = models.CharField(max_length=50, blank=True, null=True)
    league_rank = models.IntegerField(blank=True, null=True)
    overall = models.IntegerField(blank=True, null=True)
    potential = models.IntegerField(blank=True, null=True)
    value_eur = models.IntegerField(blank=True, null=True)
    wage_eur = models.IntegerField(blank=True, null=True)
    preferred_foot = models.CharField(max_length=50, blank=True, null=True)
    international_reputation = models.IntegerField(blank=True, null=True)
    weak_foot = models.IntegerField(blank=True, null=True)
    skill_moves = models.IntegerField(blank=True, null=True)
    work_rate = models.CharField(max_length=50, blank=True, null=True)
    body_type = models.CharField(max_length=50, blank=True, null=True)
    real_face = models.CharField(max_length=50, blank=True, null=True)
    release_clause_eur = models.IntegerField(blank=True, null=True)
    player_tags = models.CharField(max_length=-1, blank=True, null=True)
    team_jersey_number = models.IntegerField(blank=True, null=True)
    loaned_from = models.CharField(max_length=50, blank=True, null=True)
    joined = models.DateField(blank=True, null=True)
    contract_valid_until = models.IntegerField(blank=True, null=True)
    nation_position = models.CharField(max_length=50, blank=True, null=True)
    nation_jersey_number = models.IntegerField(blank=True, null=True)
    player_traits = models.CharField(max_length=-1, blank=True, null=True)
    pace = models.IntegerField(blank=True, null=True)
    shooting = models.IntegerField(blank=True, null=True)
    passing = models.IntegerField(blank=True, null=True)
    dribbling = models.IntegerField(blank=True, null=True)
    defending = models.IntegerField(blank=True, null=True)
    physic = models.IntegerField(blank=True, null=True)
    gk_diving = models.IntegerField(blank=True, null=True)
    gk_handling = models.IntegerField(blank=True, null=True)
    gk_kicking = models.IntegerField(blank=True, null=True)
    gk_reflexes = models.IntegerField(blank=True, null=True)
    gk_speed = models.IntegerField(blank=True, null=True)
    gk_positioning = models.IntegerField(blank=True, null=True)
    attacking_crossing = models.IntegerField(blank=True, null=True)
    attacking_finishing = models.IntegerField(blank=True, null=True)
    attacking_heading_accuracy = models.IntegerField(blank=True, null=True)
    attacking_short_passing = models.IntegerField(blank=True, null=True)
    attacking_volleys = models.IntegerField(blank=True, null=True)
    skill_dribbling = models.IntegerField(blank=True, null=True)
    skill_curve = models.IntegerField(blank=True, null=True)
    skill_fk_accuracy = models.IntegerField(blank=True, null=True)
    skill_long_passing = models.IntegerField(blank=True, null=True)
    skill_ball_control = models.IntegerField(blank=True, null=True)
    movement_acceleration = models.IntegerField(blank=True, null=True)
    movement_sprint_speed = models.IntegerField(blank=True, null=True)
    movement_agility = models.IntegerField(blank=True, null=True)
    movement_reactions = models.IntegerField(blank=True, null=True)
    movement_balance = models.IntegerField(blank=True, null=True)
    power_shot_power = models.IntegerField(blank=True, null=True)
    power_jumping = models.IntegerField(blank=True, null=True)
    power_stamina = models.IntegerField(blank=True, null=True)
    power_strength = models.IntegerField(blank=True, null=True)
    power_long_shots = models.IntegerField(blank=True, null=True)
    mentality_aggression = models.IntegerField(blank=True, null=True)
    mentality_interceptions = models.IntegerField(blank=True, null=True)
    mentality_positioning = models.IntegerField(blank=True, null=True)
    mentality_vision = models.IntegerField(blank=True, null=True)
    mentality_penalties = models.IntegerField(blank=True, null=True)
    mentality_composure = models.IntegerField(blank=True, null=True)
    defending_marking = models.IntegerField(blank=True, null=True)
    defending_standing_tackle = models.IntegerField(blank=True, null=True)
    defending_sliding_tackle = models.IntegerField(blank=True, null=True)
    goalkeeping_diving = models.IntegerField(blank=True, null=True)
    goalkeeping_handling = models.IntegerField(blank=True, null=True)
    goalkeeping_kicking = models.IntegerField(blank=True, null=True)
    goalkeeping_positioning = models.IntegerField(blank=True, null=True)
    goalkeeping_reflexes = models.IntegerField(blank=True, null=True)
    ls = models.IntegerField(blank=True, null=True)
    st = models.IntegerField(blank=True, null=True)
    rs = models.IntegerField(blank=True, null=True)
    lw = models.IntegerField(blank=True, null=True)
    lf = models.IntegerField(blank=True, null=True)
    cf = models.IntegerField(blank=True, null=True)
    rf = models.IntegerField(blank=True, null=True)
    rw = models.IntegerField(blank=True, null=True)
    lam = models.IntegerField(blank=True, null=True)
    cam = models.IntegerField(blank=True, null=True)
    ram = models.IntegerField(blank=True, null=True)
    lm = models.IntegerField(blank=True, null=True)
    lcm = models.IntegerField(blank=True, null=True)
    cm = models.IntegerField(blank=True, null=True)
    rcm = models.IntegerField(blank=True, null=True)
    rm = models.IntegerField(blank=True, null=True)
    lwb = models.IntegerField(blank=True, null=True)
    ldm = models.IntegerField(blank=True, null=True)
    cdm = models.IntegerField(blank=True, null=True)
    rdm = models.IntegerField(blank=True, null=True)
    rwb = models.IntegerField(blank=True, null=True)
    lb = models.IntegerField(blank=True, null=True)
    lcb = models.IntegerField(blank=True, null=True)
    cb = models.IntegerField(blank=True, null=True)
    rcb = models.IntegerField(blank=True, null=True)
    rb = models.IntegerField(blank=True, null=True)
    positionid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Fact.PlayerStats'


class OldPlayerstats(models.Model):
    id = models.BigIntegerField(primary_key=True)
    sofifa_id = models.IntegerField()
    year = models.IntegerField()
    player_url = models.CharField(max_length=200, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    height_cm = models.IntegerField(blank=True, null=True)
    weight_kg = models.IntegerField(blank=True, null=True)
    nationality = models.CharField(max_length=50, blank=True, null=True)
    club_name = models.CharField(max_length=50, blank=True, null=True)
    league_name = models.CharField(max_length=50, blank=True, null=True)
    league_rank = models.IntegerField(blank=True, null=True)
    overall = models.IntegerField(blank=True, null=True)
    potential = models.IntegerField(blank=True, null=True)
    value_eur = models.IntegerField(blank=True, null=True)
    wage_eur = models.IntegerField(blank=True, null=True)
    preferred_foot = models.CharField(max_length=50, blank=True, null=True)
    international_reputation = models.IntegerField(blank=True, null=True)
    weak_foot = models.IntegerField(blank=True, null=True)
    skill_moves = models.IntegerField(blank=True, null=True)
    work_rate = models.CharField(max_length=50, blank=True, null=True)
    body_type = models.CharField(max_length=50, blank=True, null=True)
    real_face = models.CharField(max_length=50, blank=True, null=True)
    release_clause_eur = models.IntegerField(blank=True, null=True)
    player_tags = models.CharField(max_length=-1, blank=True, null=True)
    team_position = models.CharField(max_length=50, blank=True, null=True)
    team_jersey_number = models.IntegerField(blank=True, null=True)
    loaned_from = models.CharField(max_length=50, blank=True, null=True)
    joined = models.DateField(blank=True, null=True)
    contract_valid_until = models.IntegerField(blank=True, null=True)
    nation_position = models.CharField(max_length=50, blank=True, null=True)
    nation_jersey_number = models.IntegerField(blank=True, null=True)
    player_traits = models.CharField(max_length=-1, blank=True, null=True)
    pace = models.IntegerField(blank=True, null=True)
    shooting = models.IntegerField(blank=True, null=True)
    passing = models.IntegerField(blank=True, null=True)
    dribbling = models.IntegerField(blank=True, null=True)
    defending = models.IntegerField(blank=True, null=True)
    physic = models.IntegerField(blank=True, null=True)
    gk_diving = models.IntegerField(blank=True, null=True)
    gk_handling = models.IntegerField(blank=True, null=True)
    gk_kicking = models.IntegerField(blank=True, null=True)
    gk_reflexes = models.IntegerField(blank=True, null=True)
    gk_speed = models.IntegerField(blank=True, null=True)
    gk_positioning = models.IntegerField(blank=True, null=True)
    attacking_crossing = models.IntegerField(blank=True, null=True)
    attacking_finishing = models.IntegerField(blank=True, null=True)
    attacking_heading_accuracy = models.IntegerField(blank=True, null=True)
    attacking_short_passing = models.IntegerField(blank=True, null=True)
    attacking_volleys = models.IntegerField(blank=True, null=True)
    skill_dribbling = models.IntegerField(blank=True, null=True)
    skill_curve = models.IntegerField(blank=True, null=True)
    skill_fk_accuracy = models.IntegerField(blank=True, null=True)
    skill_long_passing = models.IntegerField(blank=True, null=True)
    skill_ball_control = models.IntegerField(blank=True, null=True)
    movement_acceleration = models.IntegerField(blank=True, null=True)
    movement_sprint_speed = models.IntegerField(blank=True, null=True)
    movement_agility = models.IntegerField(blank=True, null=True)
    movement_reactions = models.IntegerField(blank=True, null=True)
    movement_balance = models.IntegerField(blank=True, null=True)
    power_shot_power = models.IntegerField(blank=True, null=True)
    power_jumping = models.IntegerField(blank=True, null=True)
    power_stamina = models.IntegerField(blank=True, null=True)
    power_strength = models.IntegerField(blank=True, null=True)
    power_long_shots = models.IntegerField(blank=True, null=True)
    mentality_aggression = models.IntegerField(blank=True, null=True)
    mentality_interceptions = models.IntegerField(blank=True, null=True)
    mentality_positioning = models.IntegerField(blank=True, null=True)
    mentality_vision = models.IntegerField(blank=True, null=True)
    mentality_penalties = models.IntegerField(blank=True, null=True)
    mentality_composure = models.IntegerField(blank=True, null=True)
    defending_marking = models.IntegerField(blank=True, null=True)
    defending_standing_tackle = models.IntegerField(blank=True, null=True)
    defending_sliding_tackle = models.IntegerField(blank=True, null=True)
    goalkeeping_diving = models.IntegerField(blank=True, null=True)
    goalkeeping_handling = models.IntegerField(blank=True, null=True)
    goalkeeping_kicking = models.IntegerField(blank=True, null=True)
    goalkeeping_positioning = models.IntegerField(blank=True, null=True)
    goalkeeping_reflexes = models.IntegerField(blank=True, null=True)
    ls = models.IntegerField(blank=True, null=True)
    st = models.IntegerField(blank=True, null=True)
    rs = models.IntegerField(blank=True, null=True)
    lw = models.IntegerField(blank=True, null=True)
    lf = models.IntegerField(blank=True, null=True)
    cf = models.IntegerField(blank=True, null=True)
    rf = models.IntegerField(blank=True, null=True)
    rw = models.IntegerField(blank=True, null=True)
    lam = models.IntegerField(blank=True, null=True)
    cam = models.IntegerField(blank=True, null=True)
    ram = models.IntegerField(blank=True, null=True)
    lm = models.IntegerField(blank=True, null=True)
    lcm = models.IntegerField(blank=True, null=True)
    cm = models.IntegerField(blank=True, null=True)
    rcm = models.IntegerField(blank=True, null=True)
    rm = models.IntegerField(blank=True, null=True)
    lwb = models.IntegerField(blank=True, null=True)
    ldm = models.IntegerField(blank=True, null=True)
    cdm = models.IntegerField(blank=True, null=True)
    rdm = models.IntegerField(blank=True, null=True)
    rwb = models.IntegerField(blank=True, null=True)
    lb = models.IntegerField(blank=True, null=True)
    lcb = models.IntegerField(blank=True, null=True)
    cb = models.IntegerField(blank=True, null=True)
    rcb = models.IntegerField(blank=True, null=True)
    rb = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Old.PlayerStats'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
