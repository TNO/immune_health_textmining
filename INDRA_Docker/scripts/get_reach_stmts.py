# def do_something(data_path, out_path, wildcard):
    # print(data_path)
    # print(out_path)
    # print(wildcard)
# do_something(snakemake.input[0], snakemake.output[0], snakemake.wildcards)

## IMPORTS:
import io
import os
import re
import shutil

from nltk.tokenize import sent_tokenize

from indra.sources import trips
from indra.sources import reach

def create_folders():

    if not os.path.exists("output/reach"):
        os.makedirs("output/reach")
    if not os.path.exists("output/trips"):
        os.makedirs("output/trips")
    if not os.path.exists("/workdir/output/"):
        os.makedirs("/workdir/output/")
    if not os.path.exists("/workdir/output/stmts_output/"):
        os.makedirs("/workdir/output/stmts_output/")

def process_indra():
    filename = snakemake.input[0]
    print(filename)
    
    input_dir = "/workdir/input/"
    output_dir = "/workdir/output/"
    
    literature_stmts_rp = []
    literature_stmts_tp = []

    if not os.path.exists(output_dir + "batch_output/"):
        os.makedirs(output_dir + "batch_output/")
    if not os.path.exists(output_dir + "indra_output/"):
        os.makedirs(output_dir + "indra_output/")

    with open(output_dir + "stmts_output/" + "stmts_trips.txt", "a") as trips_output:
        with open(output_dir + "stmts_output/" + "stmts_reach.txt", "a") as reach_output:

            filename = filename.split('/')[-1].split('_output.txt')[0]
            
            with open(input_dir + filename + "_output.txt") as infile:

                text = infile.readline()
                sent_tokenize_list = sent_tokenize(text)
#                 print("Total sentences: ", len(sent_tokenize_list))
                sentence_count = 0

                for sentence in sent_tokenize_list:
                    sentence_count += 1
#                     print("Sentence Count: ", sentence_count)

                    ## REACH
                    if not os.path.exists(output_dir + "reach/stmts/"):
                        os.makedirs(output_dir + "reach/stmts/")
                    if not os.path.exists(output_dir + "reach/no_stmts/"):
                        os.makedirs(output_dir + "reach/no_stmts/")

                    reach_stmts = output_dir + "reach/stmts/" + filename + "_" + str(sentence_count) + ".json"
                    reach_no_stmts = output_dir+ "reach/no_stmts/" + filename + "_" + str(sentence_count) + ".json"

                    # check if file exists
                    if not os.path.isfile(reach_stmts) and not os.path.isfile(reach_no_stmts):
                        rp = reach.process_text(sentence,  offline=True, output_fname=output_dir+"indra_output/"+filename+"_"+str(sentence_count)+".json")
                        if rp.statements:
                            print(rp.statements)
                            literature_stmts_rp += rp.statements
                            reach_output.write(str(rp.statements) + '\n')
                            shutil.move(output_dir + "indra_output/" + filename + "_" + str(sentence_count) + ".json",
                                reach_stmts)
                        else:
                            shutil.move(output_dir + "indra_output/" + filename + "_" + str(sentence_count) + ".json",
                                reach_no_stmts)

            print("Finished: "+filename)
            with open(output_dir + "processed/reach/" + filename + ".json","w") as jsonfile:
                jsonfile.write(str(reach_stmts))
#             print(directory + "output/" + filename + ".xml")
#             with open(directory + "output/" + filename + ".xml", "w") as xmlfile:
#                 xmlfile.write(str(trips_stmts))


if __name__ == '__main__':
    create_folders()
    process_indra()