import glob


def display_png():
  png_files = glob.glob("*.png")
  print(png_files)


def display_flowcharts():
  flowchart_file = glob.glob("*.flowchart*")
  print(flowchart_file)


def display_flowchart_subdir():
    flowchar_files = glob.iglob("**/*flowcharts*", recursive=True)
    for file in flowchar_files:
        print(file)
