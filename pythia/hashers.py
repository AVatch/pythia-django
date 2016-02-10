import safeid

from django.conf import settings
from django.contrib.auth.hashers import BasePasswordHasher

class PythiaSafeIDHasher(BasePasswordHasher):
    algorithm = "pythia"

    def encode(self, password, salt):
        w, t, z, p = safeid.new(password)
        
        print "password: %s" % type(password)
        print "w: %s" % type(w)
        print "t: %s" % type(t)
        print "z: %s" % type(z)
        print "p: %s" % type(p)
        
        encoded = "%s$%s$%s$%s$%s" % (self.algorithm, w, t, z, p)
        print "encoded: %s" % type(encoded)
        
        return "%s$%s$%s$%s$%s" % (self.algorithm, w, t, z, p)

    def verify(self, password, encoded):
        
        print "encoded: %s" % type(encoded)
        algorith, w, t, z, p = encoded.split('$', 5)
    
        print "password: %s" % type(password)
        print "w: %s" % type(w)
        print "t: %s" % type(t)
        print "z: %s" % type(z)
        print "p: %s" % type(p)
        
        
        password = str(password)
        w = str(w)
        t = str(t)
        z = str(z)
        p = str(p)
        
        print "password: %s" % type(password)
        print "w: %s" % type(w)
        print "t: %s" % type(t)
        print "z: %s" % type(z)
        print "p: %s" % type(p)
        
        
    
        # print 'password: %s\nw: %s\nt: %s\nz: %s\np: %s' % (password, w, t, z, p)
        return safeid.check(password, w, t, z, p)
