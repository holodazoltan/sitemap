'''
Parse sitemap and write it to csv file
'''

import csv
import argparse
from usp.tree import sitemap_tree_for_homepage

def write_csv(tree, csv_file):
  with open(csv_file, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow(['url','priority','last_modified'])
    for line in tree.all_pages():
      writer.writerow([line.url,str(line.priority),str(line.last_modified)])

if __name__ == '__main__':
  parser = argparse.ArgumentParser(
    description="Generate sitemap csv from given url")
  parser.add_argument('--url', default="http://www.freshdirect.com/")
  parser.add_argument('--csv', default="sitemap.csv")

  args = parser.parse_args()
  print(args)

  tree = sitemap_tree_for_homepage(args.url)
  write_csv(tree, args.csv)
