from dijsktra import Graph
    
def run_sample():
  edges = [
   #("A","B",6),
   ("FL","BO",465),
   ("FL","NY",299),
   ("FL","LV",99),
   ("FL","LA",676),
   ("LA","LV",169),
   ("LA","SLC",222),
   ("LV","NY",617),
   ("LV","VC",327),
   ("LV","CH",254),
   ("SLC","LA",222),
   ("VC","BO",561),
   ("VC","NY",603),
   ("MN","NY",237),
   ("CH","NY",226),
  ]
  
  graph = Graph(edges)
  start = 'SLC'
  stop = 'BO'
  path = graph.dijsktra_shortest_path(start, stop)
  print (path)
  print("This is how many layover(s) you have.")
  print(len(path) - 2)
  
  

def main():
  run_sample()

if __name__ == "__main__":
  main()
  