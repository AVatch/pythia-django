import safeid

from django.conf import settings
from django.contrib.auth.hashers import BasePasswordHasher


class PythiaSafeIDHasher(BasePasswordHasher):
    algorithm = "pythia"

    def encode(self, password, salt):
        w, t, z, p = safeid.new(password)
        return  "%s$%s$%s$%s$%s" %  (self.algorithm, w, t, z, p)

    def verify(self, password, encoded):
        algorith, w, t, z, p = encoded.split('$', 5)
        return safeid.check(password, w, t, z, p)
        
