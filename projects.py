def setup():
  name = "E-commerce"
  kian = "https://flaskportfolio.komaysugiyama.repl.co/"
  komay = "https://flaskportfolio.komaysugiyama.repl.co/"
  chris = "https://repl.it/@ChristopherRub1/flaskportfolio-1#templates/home.html"
  megan = "https://megan-website.megancorrigan.repl.co/"
  ridhima = "https://repl.it/join/uvlcpsqd-ridhimainukurt1"
  Kianvid = "https://www.loom.com/embed/73f8ec847fb04f49996feccaef3950a0"
  Komayvid = "https://www.youtube.com/embed/pdxepGaS3yM"
  Chrisvid = "https://www.youtube.com/embed/9tOJYbQ962E?start=0&end=60"
  Meganvid = "https://www.youtube.com/embed/XSGg-K97ei8"
  Ridhimavid = "https://www.youtube.com/embed/q73j4E9OpHk"
  source = {"name": name, "kian": kian, "komay": komay, "chris": chris, "megan": megan, "ridhima": ridhima, "Kianvid":Kianvid, "Komayvid":Komayvid, "Chrisvid":Chrisvid, "Meganvid":Meganvid, "Ridhimavid":Ridhimavid}
  #Project Data
  project1 =  "Hello Series"
  projlinks1 = [
    Link("Project Plan", "http://nighthawkcoders.cf/courses/python/"),
    Link("Repl", "https://repl.it/@jmort1021/Python-Hello-Series#README.md"),
    Link("Resources", "https://padlet.com/jmortensen7/csp2021")
  ]
  project2 =  "Flask Project"
  projlinks2 = [
    Link("Project Plan", "http://nighthawkcoders.cf/courses/python/"),
    Link("Repl", "https://repl.it/@jmort1021/Python-Web-Portfolio-Series?__cf_chl_jschl_tk__=cff72504752e89d50dea999ce10f859a17ecc294-1603026111-0-AdBP5FO-3nyUc_KVdPlNwvXM4MwUXy1HXHmbiJui1YBnUTPJZ8X4UBZVeYUXrnwRBJVvku9NftGYDWtp8lp4KovKX55R8S4twedzHpa2snwLwoAWaxuc4rgAa2l9J_rWqnNvUNcjJ8-p1V1RuTWV3lIy149lptozqAQdJnGj7PlcJxnu3YH22EXK-jl7bmdQmW9r_9fE1xp8J7sOFS3I1PMgmtoExcDIQSBBTnx1zQsyQGNS6wnuX72MAPnS_x3ZL1ETNRgFbVKpLsFJiR9ED1ErU54wyZYrUxEbZ_txHd7qY1T_s_lE6Ll8jYWHx-GulQ#main.py"),
    Link("Resources", "https://padlet.com/jmortensen7/csptime1_2")
  ]
  #Project Objects
  proj1 = Project(project1, projlinks1)
  proj2 = Project(project2, projlinks2)
  #HTML Data
  projects = Projects(source, [proj1, proj2])
  return projects

class Link():
  #link data with button and href (url)
  def __init__(self, btn, href):
    self.btn = btn
    self.href = href
  def get_btn(self):
    return self.btn
  def get_href(self):
    return self.href

class Project():
  #project data with name and links
  def __init__(self, name, links):
    self.name = name
    self.links = links
  def get_name(self):
    return self.name
  def get_links(self):
    return self.links

class Projects():
  #HTML data with source and projects    
  def __init__(self, source, projects):
    self.source = source
    self.projects = projects
  #source data getter
  def get_source(self):
    return self.source
  #project data getter
  def get_projects(self):
    return self.projects