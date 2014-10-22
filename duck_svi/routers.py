from duck_svi.models import WishSvi


class SviRouter(object):
    """
    A router to check if its an svi object to push in the good database
    """

    def db_for_read(self, model, **hints):
        """
        Attempts to read auth models go to svi.
        """
        if model.__name__ == WishSvi.__name__:
            return 'svi'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write auth models go to auth_db.
        """
        if model.__name__ == WishSvi.__name__:
            return 'svi'
        return None

    # def allow_relation(self, obj1, obj2, **hints):
    #     """
    #     Allow relations if a model in the auth app is involved.
    #     """
    #     if model.__class__.__name__ == 'WishSvi':
    #          return True
    #     return None

    # def allow_syncdb(self, db, model):
    #     """
    #     Make sure the auth app only appears in the 'auth_db'
    #     database.
    #     """
    #     if db == 'auth_db':
    #         return model._meta.app_label == 'auth'
    #     elif model._meta.app_label == 'auth':
    #         return False
    #     return None