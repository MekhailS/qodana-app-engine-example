from google.appengine.ext import db

# IndexRequiredQueryInspection
group_name = 'foo'

VALID_QUERY = db.GqlQuery("SELECT __key__ FROM MessageIndex WHERE group_name = :1 ORDER BY created_at DESC", group_name).fetch(1)

INVALID_QUERY_NOT_EXISTING_NAME = db.GqlQuery("SELECT __key__ FROM MessageIndex WHERE not_existing_name = :1 ORDER BY created_at DESC", group_name).fetch(1)

VALID_SIMPLE_QUERY = db.GqlQuery("SELECT * FROM Greeting ORDER BY date DESC LIMIT 10")

VALID_ORDER_BY_KEY_QUERY = db.GqlQuery("SELECT * FROM Subscription WHERE group_name = :1 AND notification_type IN :2 ORDER BY __key__", group_name, [1, 2])

# QueryBoundParametersInspection
INVALID_NOT_ENOUGH_PARAMETERS_QUERY = db.GqlQuery("SELECT __key__ FROM MessageIndex WHERE group_name = :1 AND created_at <= :2 ORDER BY created_at DESC", group_name)

# RestrictedQueryInspection
INEQUALITY_FILTERS = db.GqlQuery("SELECT * FROM Person WHERE birth_year >= :min_year AND height >= :min_height")

INEQUALITY_ORDER = db.GqlQuery('SELECT * FROM Person WHERE birth_year >= :min_year ORDER BY last_name')

# SandboxInspection
NO_OPEN_IN_GOOGLE_APP_ENGINE = open("x.txt", "w")
