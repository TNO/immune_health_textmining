import io
import os
import re
import shutil

from nltk.tokenize import sent_tokenize

from indra.sources import eidos

def create_folders():

    if not os.path.exists("output/eidos/"):
        os.makedirs("output/eidos/")
    if not os.path.exists("/workdir/output/"):
        os.makedirs("/workdir/output/")
    if not os.path.exists("/workdir/output/stmts_output/"):
        os.makedirs("/workdir/output/stmts_output/")

def process_indra():
    filename = snakemake.input[0]
    print(filename)
    
    input_dir = "/workdir/input/"
    output_dir = "/workdir/output/"
    
    literature_stmts_ep = []
    literature_stmts_tp = []

    if not os.path.exists(output_dir + "batch_output/"):
        os.makedirs(output_dir + "batch_output/")
    if not os.path.exists(output_dir + "indra_output/"):
        os.makedirs(output_dir + "indra_output/")

    with open(output_dir + "stmts_output/" + "stmts_trips.txt", "a") as trips_output:
        with open(output_dir + "stmts_output/" + "stmts_eidos.txt", "a") as eidos_output:

            filename = filename.split('/')[-1].split('_output.txt')[0]
            
            with open(input_dir + filename + "_output.txt") as infile:

                text = infile.readline()
                sent_tokenize_list = sent_tokenize(text)
#                 print("Total sentences: ", len(sent_tokenize_list))
                sentence_count = 0

                for sentence in sent_tokenize_list:
                    sentence_count += 1
#                     print("Sentence Count: ", sentence_count)

                    ## EIDOS
                    if not os.path.exists(output_dir + "eidos/stmts/"):
                        os.makedirs(output_dir + "eidos/stmts/")
                    if not os.path.exists(output_dir + "eidos/no_stmts/"):
                        os.makedirs(output_dir + "eidos/no_stmts/")

                    eidos_stmts = output_dir + "eidos/stmts/" + filename + "_" + str(sentence_count) + ".json"
                    eidos_no_stmts = output_dir+ "eidos/no_stmts/" + filename + "_" + str(sentence_count) + ".json"

                    # check if file exists
                    if not os.path.isfile(eidos_stmts) and not os.path.isfile(eidos_no_stmts):
                        ep = eidos.process_text(sentence, save_json=output_dir+"indra_output/"+filename+"_"+str(sentence_count)+".json")
                        if ep.statements:
                            print(ep.statements)
                            literature_stmts_ep += ep.statements
                            eidos_output.write(str(ep.statements) + '\n')
                            shutil.move(output_dir + "indra_output/" + filename + "_" + str(sentence_count) + ".json",
                                eidos_stmts)
                        else:
                            shutil.move(output_dir + "indra_output/" + filename + "_" + str(sentence_count) + ".json",
                                eidos_no_stmts)

            print("Finished: "+filename)
            with open(output_dir + "processed/eidos/" + filename + ".json","w") as jsonfile:
                jsonfile.write(str(eidos_stmts))



if __name__ == '__main__':
    create_folders()
    process_indra()