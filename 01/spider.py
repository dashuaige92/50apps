from lxml import html
import urllib2
import re

class Spider(object):
    """Crawls a website to a given depth"""
    def __init__(self):
        pass

    def crawl(self, url, depth=1, query=''):
        """Crawls url to given depth
        returns a list of all urls encountered"""
        matches = []
        prev_urls = [url]
        for i in range(depth+1):
            next_urls = []
            for link in prev_urls:
                try:
                    data = urllib2.urlopen(link)
                    tree = html.parse(data)
                    for a in tree.xpath('//a/@href'):
                        if '#' in a[:2]:
                            next
                        if re.match('https?:\/\/', a):
                            a_url = a
                        elif len(a) and a[0] == '/':
                            a_url = link[:link.find('/', 7)] + a
                        else:
                            a_url = link.rstrip('/') + '/' + a
                        if a_url not in next_urls:
                            next_urls += [a_url]
                    if tree.xpath('string()').count(query):
                    #if True:
                        matches += [link]
                        print "@" + next_urls[len(next_urls)-1]
                    else:
                        print "!" + next_urls[len(next_urls)-1]
                except (urllib2.HTTPError, urllib2.URLError):
                    print "Can't load " + link
            prev_urls = next_urls
            print("Depth: " + str(i) + "\tCount: " + str(len(prev_urls)))
        return matches

def main(argv=None):
    if argv is None:
        import sys
        argv = sys.argv
    s = Spider()
    if len(argv) < 2: argv += ['http://google.com']
    if len(argv) < 3: argv += ['1']
    print "Crawling " + argv[1] + " with depth " + argv[2]
    print s.crawl(argv[1], int(argv[2]))

if __name__ == '__main__':
    main()

