# -*- coding: iso-8859-1 -*-

###############################################################################
### LICENSE
###############################################################################
#
# findmyhash.py - v 1.1.2
#
# This script is under GPL v3 License
# (http://www.gnu.org/licenses/gpl-3.0.html).
#
# Only this source code is under GPL v3 License. Web services used in this
# script are under different licenses.
#
# If you know some clause in one of these web services which forbids to use
# it inside this script,
# please contact me to remove the web service as soon as possible.
#
# Developed by JulGor ( http://laxmarcaellugar.blogspot.com/ )
# Mail: bloglaxmarcaellugar AT gmail DOT com
# twitter: @laXmarcaellugar
#

try:
    import sys
    import hashlib
    import urllib2
    import getopt
    from os import path
    from urllib import urlencode
    from re import search, findall
    from random import seed, randint
    from base64 import decodestring
    from cookielib import LWPCookieJar
except:
    print """
Execution error:

  You required some basic Python libraries.

  This application use: sys, hashlib, urllib, urllib2, os, re, random, getopt, base64 and cookielib.

  Please, check if you have all of them installed in your system.

"""
    sys.exit(1)

try:
    from httplib2 import Http
except:
    print """
Execution error:

  The Python library httplib2 is not installed in your system.
  Please, install it before use this application.

"""
    sys.exit(1)

try:
    from libxml2 import parseDoc
except:
    print """
Execution error:

  The Python library libxml2 is not installed in your system.

  Because of that, some plugins aren't going to work correctly.

  Please, install it before use this application.

"""

MD4 = "md4"
MD5 = "md5"
SHA1 = "sha1"
SHA224 = "sha224"
SHA256 = "sha256"
SHA384 = "sha384"
SHA512 = "sha512"
RIPEMD = "rmd160"
LM = "lm"
NTLM = "ntlm"
MYSQL = "mysql"
CISCO7 = "cisco7"
JUNIPER = "juniper"
GOST = "gost"
WHIRLPOOL = "whirlpool"
LDAP_MD5 = "ldap_md5"
LDAP_SHA1 = "ldap_sha1"


USER_AGENTS = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; \
        SV1; Crazy Browser 1.0.5)",
    "curl/7.7.2 (powerpc-apple-darwin6.0) libcurl 7.7.2 (OpenSSL 0.9.6b)",
    "Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 \
        Firefox/5.0",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b8pre) Gecko/20101213 \
        Firefox/4.0b8pre",
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 7.1; Trident/5.0)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0) \
        chromeframe/10.0.648.205",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; \
        InfoPath.2; SLCC1; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; \
        .NET CLR 2.0.50727)",
    "Opera/9.80 (Windows NT 6.1; U; sv) Presto/2.7.62 Version/11.01",
    "Opera/9.80 (Windows NT 6.1; U; pl) Presto/2.7.62 Version/11.00",
    "Opera/9.80 (X11; Linux i686; U; pl) Presto/2.6.30 Version/10.61",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.2 \
        (KHTML, like Gecko) Chrome/15.0.861.0 Safari/535.2",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.2 (KHTML, like Gecko) \
        Chrome/15.0.872.0 Safari/535.2",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.1 (KHTML, like Gecko) \
        Chrome/14.0.812.0 Safari/535.1",
    "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
]


class NETMD5CRACK:
    name = "netmd5crack"
    url = "http://www.netmd5crack.com"
    supported_algorithm = [MD5]

    def isSupported(self, alg):
        """Return True if HASHCRACK can crack this type of algorithm and
        False if it cannot."""

        if alg in self.supported_algorithm:
            return True
        else:
            return False

    def crack(self, hashvalue, alg):
        """Try to crack the hash.
        @param hashvalue Hash to crack.
        @param alg Algorithm to crack."""

        # Check if the cracker can crack this kind of algorithm
        if not self.isSupported(alg):
            return None

        # Build the URL
        url = "http://www.netmd5crack.com/cgi-bin/Crack.py?InputHash=%s" % (hashvalue)

        # Make the request
        response = do_HTTP_request(url)

        # Analyze the response
        html = None
        if response:
            html = response.read()
        else:
            return None

        regexp = r'<tr><td class="border">%s</td><td class="border">[^<]*</td></tr></table>' % (hashvalue)
        match = search(regexp, html)

        if match:
            match2 = search("Sorry, we don't have that hash in our database", match.group())
            if match2:
                return None
            else:
                return match.group().split('border')[2].split('<')[0][2:]


class MY_ADDR:
    name = "my-addr"
    url = "http://md5.my-addr.com"
    supported_algorithm = [MD5]

    def isSupported(self, alg):
        """Return True if HASHCRACK can crack this type of algorithm and
        False if it cannot."""

        if alg in self.supported_algorithm:
            return True
        else:
            return False

    def crack(self, hashvalue, alg):
        """Try to crack the hash.
        @param hashvalue Hash to crack.
        @param alg Algorithm to crack."""

        # Check if the cracker can crack this kind of algorithm
        if not self.isSupported(alg):
            return None

        # Build the URL
        url = "http://md5.my-addr.com/md5_decrypt-md5_cracker_online/md5_decoder_tool.php"

        # Build the parameters
        params = {
            "md5": hashvalue,
            "x": 21,
            "y": 8
        }

        # Make the request
        response = do_HTTP_request(url, params)

        # Analyze the response
        html = None
        if response:
            html = response.read()
        else:
            return None

        match = search(r"<span class='middle_title'>Hashed string</span>: [^<]*</div>", html)

        if match:
            return match.group().split('span')[2][3:-6]
        else:
            return None


class MD5PASS:
    name = "md5pass"
    url = "http://md5pass.info"
    supported_algorithm = [MD5]

    def isSupported(self, alg):
        """Return True if HASHCRACK can crack this type of algorithm and
        False if it cannot."""

        if alg in self.supported_algorithm:
            return True
        else:
            return False

    def crack(self, hashvalue, alg):
        """Try to crack the hash.
        @param hashvalue Hash to crack.
        @param alg Algorithm to crack."""

        # Check if the cracker can crack this kind of algorithm
        if not self.isSupported(alg):
            return None

        # Build the URL
        url = self.url

        # Build the parameters
        params = {
            "hash": hashvalue,
            "get_pass": "Get Pass"
        }

        # Make the request
        response = do_HTTP_request(url, params)

        # Analyze the response
        html = None
        if response:
            html = response.read()
        else:
            return None

        match = search(r"Password - <b>[^<]*</b>", html)

        if match:
            return match.group().split('b>')[1][:-2]
        else:
            return None


class MD5DECRYPTION:
    name = "md5decryption"
    url = "http://md5decryption.com"
    supported_algorithm = [MD5]

    def isSupported(self, alg):
        """Return True if HASHCRACK can crack this type of algorithm and
        False if it cannot."""

        if alg in self.supported_algorithm:
            return True
        else:
            return False

    def crack(self, hashvalue, alg):
        """Try to crack the hash.
        @param hashvalue Hash to crack.
        @param alg Algorithm to crack."""

        # Check if the cracker can crack this kind of algorithm
        if not self.isSupported(alg):
            return None

        # Build the URL
        url = self.url

        # Build the parameters
        params = {
            "hash": hashvalue,
            "submit": "Decrypt It!"
        }

        # Make the request
        response = do_HTTP_request(url, params)

        # Analyze the response
        html = None
        if response:
            html = response.read()
        else:
            return None

        match = search(r"Decrypted Text: </b>[^<]*</font>", html)

        if match:
            return match.group().split('b>')[1][:-7]
        else:
            return None


class MD5ONLINE:
    name = "md5online"
    url = "http://md5online.net"
    supported_algorithm = [MD5]

    def isSupported(self, alg):
        """Return True if HASHCRACK can crack this type of algorithm and
        False if it cannot."""

        if alg in self.supported_algorithm:
            return True
        else:
            return False

    def crack(self, hashvalue, alg):
        """Try to crack the hash.
        @param hashvalue Hash to crack.
        @param alg Algorithm to crack."""

        # Check if the cracker can crack this kind of algorithm
        if not self.isSupported(alg):
            return None

        # Build the URL
        url = self.url

        # Build the parameters
        params = {
            "pass": hashvalue,
            "option": "hash2text",
            "send": "Submit"
        }

        # Make the request
        response = do_HTTP_request(url, params)

        # Analyze the response
        html = None
        if response:
            html = response.read()
        else:
            return None

        match = search(r'<center><p>md5 :<b>\w*</b> <br>pass : <b>[^<]*</b></p></table>', html)

        if match:
            return match.group().split('b>')[3][:-2]
        else:
            return None


class PASSWORD_DECRYPT:
    name = "password-decrypt"
    url = "http://password-decrypt.com"
    supported_algorithm = [CISCO7, JUNIPER]

    def isSupported(self, alg):
        """Return True if HASHCRACK can crack this type of algorithm and
        False if it cannot."""

        if alg in self.supported_algorithm:
            return True
        else:
            return False

    def crack(self, hashvalue, alg):
        """Try to crack the hash.
        @param hashvalue Hash to crack.
        @param alg Algorithm to crack."""

        # Check if the cracker can crack this kind of algorithm
        if not self.isSupported(alg):
            return None

        # Build the URL and the parameters
        url = ""
        params = None
        if alg == CISCO7:
            url = "http://password-decrypt.com/cisco.cgi"
            params = {
                "submit": "Submit",
                "cisco_password": hashvalue,
                "submit": "Submit"
            }
        else:
            url = "http://password-decrypt.com/juniper.cgi"
            params = {
                "submit": "Submit",
                "juniper_password": hashvalue,
                "submit": "Submit"
            }

        response = do_HTTP_request(url, params)

        html = None
        if response:
            html = response.read()
        else:
            return None

        match = search(r'Decrypted Password:&nbsp;<B>[^<]*</B> </p>', html)

        if match:
            return match.group().split('B>')[1][:-2]
        else:
            return None


class MD5_NET:
    name = "md5.net"
    url = "http://md5.net"
    supported_algorithm = [MD5]

    def isSupported(self, alg):
        """Return True if HASHCRACK can crack this type of algorithm and
        False if it cannot."""

        if alg in self.supported_algorithm:
            return True
        else:
            return False

    def crack(self, hashvalue, alg):
        """Try to crack the hash.
        @param hashvalue Hash to crack.
        @param alg Algorithm to crack."""

        # Check if the cracker can crack this kind of algorithm
        if not self.isSupported(alg):
            return None

        # Build the URL
        url = "http://www.md5.net/cracker.php"

        # Build the parameters
        params = {
            "hash": hashvalue
        }

        # Make the request
        response = do_HTTP_request(url, params)

        # Analyze the response
        html = None
        if response:
            html = response.read()
        else:
            return None

        match = search(r'<input type="text" id="hash" size="32" value="[^"]*"/>', html)

        if match:
            return match.group().split('"')[7]
        else:
            return None


class NOISETTE:
    name = "noisette.ch"
    url = "http://md5.noisette.ch"
    supported_algorithm = [MD5]

    def isSupported(self, alg):
        """Return True if HASHCRACK can crack this type of algorithm and
        False if it cannot."""

        if alg in self.supported_algorithm:
            return True
        else:
            return False

    def crack(self, hashvalue, alg):
        """Try to crack the hash.
        @param hashvalue Hash to crack.
        @param alg Algorithm to crack."""

        # Check if the cracker can crack this kind of algorithm
        if not self.isSupported(alg):
            return None

        # Build the URL
        url = "http://md5.noisette.ch/index.php"

        # Build the parameters
        params = {
            "hash": hashvalue
        }

        # Make the request
        response = do_HTTP_request(url, params)

        # Analyze the response
        html = None
        if response:
            html = response.read()
        else:
            return None

        match = search(r'<p>String to hash : <input name="text" value="[^"]+"/>', html)

        if match:
            return match.group().split('"')[3]
        else:
            return None


class STRINGFUNCTION:
    name = "stringfunction"
    url = "http://www.stringfunction.com"
    supported_algorithm = [MD5, SHA1]

    def isSupported(self, alg):
        """Return True if HASHCRACK can crack this type of algorithm and
        False if it cannot."""

        if alg in self.supported_algorithm:
            return True
        else:
            return False

    def crack(self, hashvalue, alg):
        """Try to crack the hash.
        @param hashvalue Hash to crack.
        @param alg Algorithm to crack."""

        # Check if the cracker can crack this kind of algorithm
        if not self.isSupported(alg):
            return None

        # Build the URL
        url = ""
        if alg == MD5:
            url = "http://www.stringfunction.com/md5-decrypter.html"
        else:
            url = "http://www.stringfunction.com/sha1-decrypter.html"

        # Build the parameters
        params = {
            "string": hashvalue,
            "submit": "Decrypt",
            "result": ""
            }

        # Make the request
        response = do_HTTP_request(url, params)

        # Analyze the response
        html = None
        if response:
            html = response.read()
        else:
            return None

        match = search(r'<textarea class="textarea-input-tool-b" rows="10" cols="50" name="result"[^>]*>[^<]+</textarea>', html)

        if match:
            return match.group().split('>')[1][:-10]
        else:
            return None


class GOOG_LI:
    name = "goog.li"
    url = "http://goog.li"
    supported_algorithm = [
        MD5,
        MYSQL,
        SHA1,
        SHA224,
        SHA384,
        SHA256,
        SHA512,
        RIPEMD,
        NTLM,
        GOST,
        WHIRLPOOL,
        LDAP_MD5,
        LDAP_SHA1
    ]

    def isSupported(self, alg):
        """Return True if HASHCRACK can crack this type of algorithm and
        False if it cannot."""

        if alg in self.supported_algorithm:
            return True
        else:
            return False

    def crack(self, hashvalue, alg):
        """Try to crack the hash.
        @param hashvalue Hash to crack.
        @param alg Algorithm to crack."""

        # Check if the cracker can crack this kind of algorithm
        if not self.isSupported(alg):
            return None

        hash2 = None
        if alg in [NTLM] and ':' in hashvalue:
            hash2 = hashvalue.split(':')[1]
        else:
            hash2 = hashvalue

        # Confirm the initial '*' character
        if alg == MYSQL and hash2[0] != '*':
            hash2 = '*' + hash2

        # Build the URL
        url = "http://goog.li/?q=%s" % (hash2)

        # Make the request
        response = do_HTTP_request(url)

        # Analyze the response
        html = None
        if response:
            html = response.read()
        else:
            return None

        match = search(r'<br />cleartext[^:]*: [^<]*<br />', html)

        if match:
            return match.group().split(':')[1].strip()[:-6]
        else:
            return None


CRAKERS = [
    NETMD5CRACK,
    MY_ADDR,
    MD5PASS,
    MD5DECRYPTION,
    MD5ONLINE,
    PASSWORD_DECRYPT,
    MD5_NET,
    NOISETTE,
    STRINGFUNCTION,
    GOOG_LI,
]


def configureCookieProcessor(cookiefile='/tmp/searchmyhash.cookie'):
    '''Set a Cookie Handler to accept cookies from the different Web sites.

    @param cookiefile Path of the cookie store.'''

    cookieHandler = LWPCookieJar()
    if cookieHandler is not None:
        if path.isfile(cookiefile):
            cookieHandler.load(cookiefile)

        opener = urllib2.build_opener(
            urllib2.HTTPCookieProcessor(cookieHandler)
        )
        urllib2.install_opener(opener)


def do_HTTP_request(url, params={}, httpheaders={}):
    '''
    Send a GET or POST HTTP Request.
    @return: HTTP Response
    '''

    data = {}
    request = None

    # If there is parameters, they are been encoded
    if params:
        data = urlencode(params)

        request = urllib2.Request(url, data, headers=httpheaders)
    else:
        request = urllib2.Request(url, headers=httpheaders)

    # Send the request
    try:
        response = urllib2.urlopen(request)
    except:
        return ""

    return response


def printSyntax():
    """Print application syntax."""

    print """%s 1.1.2 ( http://code.google.com/p/findmyhash/ )

Usage:
------

  python %s <algorithm> OPTIONS


Accepted algorithms are:
------------------------

  MD4       - RFC 1320
  MD5       - RFC 1321
  SHA1      - RFC 3174 (FIPS 180-3)
  SHA224    - RFC 3874 (FIPS 180-3)
  SHA256    - FIPS 180-3
  SHA384    - FIPS 180-3
  SHA512    - FIPS 180-3
  RMD160    - RFC 2857
  GOST      - RFC 5831
  WHIRLPOOL - ISO/IEC 10118-3:2004
  LM        - Microsoft Windows hash
  NTLM      - Microsoft Windows hash
  MYSQL     - MySQL 3, 4, 5 hash
  CISCO7    - Cisco IOS type 7 encrypted passwords
  JUNIPER   - Juniper Networks $9$ encrypted passwords
  LDAP_MD5  - MD5 Base64 encoded
  LDAP_SHA1 - SHA1 Base64 encoded

  NOTE: for LM / NTLM it is recommended to introduce both values with this format:
         python %s LM   -h 9a5760252b7455deaad3b435b51404ee:0d7f1f2bdeac6e574d6e18ca85fb58a7
         python %s NTLM -h 9a5760252b7455deaad3b435b51404ee:0d7f1f2bdeac6e574d6e18ca85fb58a7


Valid OPTIONS are:
------------------

  -h <hash_value>  If you only want to crack one hash, specify its value with this option.

  -f <file>        If you have several hashes, you can specify a file with one hash per line.
                   NOTE: All of them have to be the same type.

  -g               If your hash cannot be cracked, search it in Google and show all the results.
                   NOTE: This option ONLY works with -h (one hash input) option.


Examples:
---------

  -> Try to crack only one hash.
     python %s MD5 -h 098f6bcd4621d373cade4e832627b4f6

  -> Try to crack a JUNIPER encrypted password escaping special characters.
     python %s JUNIPER -h "\$9\$LbHX-wg4Z"

  -> If the hash cannot be cracked, it will be searched in Google.
     python %s LDAP_SHA1 -h "{SHA}cRDtpNCeBiql5KOQsKVyrA0sAiA=" -g

  -> Try to crack multiple hashes using a file (one hash per line).
     python %s MYSQL -f mysqlhashesfile.txt


Contact:
--------

[Web]           http://laxmarcaellugar.blogspot.com/
[Mail/Google+]  bloglaxmarcaellugar@gmail.com
[twitter]       @laXmarcaellugar
""" % ((sys.argv[0],) * 8)


def crackHash(algorithm, hashvalue=None, hashfile=None):
    """Crack a hash or all the hashes of a file.

    @param alg Algorithm of the hash (MD5, SHA1...).
    @param hashvalue Hash value to be cracked.
    @param hashfile Path of the hash file.
    @return If the hash has been cracked or not."""

    global CRAKERS

    # Cracked hashes will be stored here
    crackedhashes = []

    # Is the hash cracked?
    cracked = False

    # Only one of the two possible inputs can be setted.
    if (not hashvalue and not hashfile) or (hashvalue and hashfile):
        return False

    # hashestocrack depends on the input value
    hashestocrack = None
    if hashvalue:
        hashestocrack = [hashvalue]
    else:
        try:
            hashestocrack = open(hashfile, "r")
        except:
            print "\nIt is not possible to read input file (%s)\n" % (hashfile)
            return cracked

    for activehash in hashestocrack:
        hashresults = []

        # Standarize the hash
        activehash = activehash.strip()
        if algorithm not in [JUNIPER, LDAP_MD5, LDAP_SHA1]:
            activehash = activehash.lower()

        print "\nCracking hash: %s\n" % (activehash)

        begin = randint(0, len(CRAKERS)-1)

        for i in range(len(CRAKERS)):

            # Select the cracker
            cr = CRAKERS[(i + begin) % len(CRAKERS)]()

            if not cr.isSupported(algorithm):
                continue

            # Analyze the hash
            print "Analyzing with %s (%s)..." % (cr.name, cr.url)

            # Crack the hash
            result = None
            try:
                result = cr.crack(activehash, algorithm)
            # If it was some trouble, exit
            except:
                print "\nSomething was wrong. Please, contact us \
                to report the bug:\n\nhttps://github.com/Talanor/findmyhash\n"
                if hashfile:
                    try:
                        hashestocrack.close()
                    except:
                        pass
                return False

            # If there is any result...
            cracked = 0
            if result:

                # If it is a hashlib supported algorithm...
                if algorithm in [
                        MD4,
                        MD5,
                        SHA1,
                        SHA224,
                        SHA384,
                        SHA256,
                        SHA512,
                        RIPEMD
                        ]:
                    # Hash value is calculated to compare with cracker result
                    h = hashlib.new(algorithm)
                    h.update(result)

                    if h.hexdigest() == activehash:
                        hashresults.append(result)
                        cracked = 2

                # If it is a half-supported hashlib algorithm
                elif algorithm in [LDAP_MD5, LDAP_SHA1]:
                    alg = algorithm.split('_')[1]
                    ahash = decodestring(activehash.split('}')[1])

                    # Hash value is calculated to compare with cracker result
                    h = hashlib.new(alg)
                    h.update(result)

                    if h.digest() == ahash:
                        hashresults.append(result)
                        cracked = 2

                elif algorithm == NTLM or (algorithm == LM and ':' in activehash):
                    # NTLM Hash value is calculated to compare with cracker result
                    candidate = hashlib.new('md4', result.split()[-1].encode('utf-16le')).hexdigest()

                    # It's a LM:NTLM combination or a single NTLM hash
                    if (':' in activehash and candidate == activehash.split(':')[1]) or (':' not in activehash and candidate == activehash):
                        hashresults.append(result)
                        cracked = 2

                # If it is another algorithm, we search in all the crackers
                else:
                    hashresults.append(result)
                    cracked = 1

            # Had the hash cracked?
            if cracked:
                print "\n***** HASH CRACKED!! *****\nThe original string is: %s\n" % (result)
                # If result was verified, break
                if cracked == 2:
                    break
            else:
                print "... hash not found in %s\n" % (cr.name)

        if hashresults:
            resultlist = []
            for r in hashresults:
                if r not in resultlist:
                    resultlist.append(r)

            finalresult = ""
            if len(resultlist) > 1:
                finalresult = ', '.join(resultlist)
            else:
                finalresult = resultlist[0]

            # Valid results are stored
            crackedhashes.append((activehash, finalresult))

    if hashfile:
        try:
            hashestocrack.close()
        except:
            pass

    # Show a resume of all the cracked hashes
    print "\nThe following hashes were cracked:\n----------------------------------\n"
    print crackedhashes and "\n".join("%s -> %s" % (hashvalue, result.strip()) for hashvalue, result in crackedhashes) or "NO HASH WAS CRACKED."
    print

    return cracked


def searchHash(hashvalue):
    '''Google the hash value looking for any result which could give some clue...

    @param hashvalue The hash is been looking for.'''

    start = 0
    finished = False
    results = []

    sys.stdout.write("\nThe hash wasn't found in any database. Maybe Google has any idea...\nLooking for results...")
    sys.stdout.flush()

    while not finished:

        sys.stdout.write('.')
        sys.stdout.flush()

        # Build the URL
        url = "http://www.google.com/search?hl=en&q=%s&filter=0" % (hashvalue)
        if start:
            url += "&start=%d" % (start)

        # Build the Headers with a random User-Agent
        headers = {"User-Agent": USER_AGENTS[randint(0, len(USER_AGENTS))-1]}

        # Send the request
        response = do_HTTP_request(url, httpheaders=headers)

        # Extract the results ...
        html = None
        if response:
            html = response.read()
        else:
            continue

        resultlist = findall(r'<a href="[^"]*?" class=l', html)

        # ... saving only new ones
        new = False
        for r in resultlist:
            url_r = r.split('"')[1]

            if not url_r in results:
                results.append(url_r)
                new = True

        start += len(resultlist)

        # If there is no a new result, finish
        if not new:
            finished = True

    if results:
        print "\n\nGoogle has some results. Maybe you would like to check them manually:\n"

        results.sort()
        for r in results:
            print "  *> %s" % (r)
        print

    else:
        print "\n\nGoogle doesn't have any result. Sorry!\n"


def main():
    """Main method."""

    if len(sys.argv) < 4:
        printSyntax()
        sys.exit(1)

    else:
        try:
            opts, args = getopt.getopt(sys.argv[2:], "gh:f:")
        except:
            printSyntax()
            sys.exit(1)

    algorithm = sys.argv[1].lower()
    hashvalue = None
    hashfile = None
    googlesearch = False

    for opt, arg in opts:
        if opt == '-h':
            hashvalue = arg
        elif opt == '-f':
            hashfile = arg
        else:
            googlesearch = True

    configureCookieProcessor()

    seed()

    cracked = 0

    cracked = crackHash(algorithm, hashvalue, hashfile)

    if not cracked and googlesearch and not hashfile:
        searchHash(hashvalue)


if __name__ == "__main__":
    main()
