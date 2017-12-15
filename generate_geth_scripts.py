import os

"""
Simple utility to generate the ethereum files I use when starting ethereum locally for testing.

Change the values below to match your installation.

0) init-genesis-block.sh

Typically, I will start 3 terminal windows:
1) start-geth-for-web.sh or start-geth.sh
2) geth-attach.sh
3) run-mist.sh

when you need to start new:
4) remove-test-data.sh or refresh-start-geth.sh


"""
# mistpath = "/Applications/Mist.app/Contents/MacOS/Mist"
# datadir = "/Users/youngsoul/blockchain/data"
# networkid = "1999"
# genesisfile = "CustomGenesis.json"

mistpath = "/Applications/Mist.app/Contents/MacOS/Mist"
datadir = "/Users/patryan/Development/blockchain/ethereum/data/ethereum_private"
networkid = "1999"
genesisfile = "/Users/patryan/Development/blockchain/ethereum/CustomGenesis.json"


def create_sh_file(template_filename, target_file):
    if os.path.exists(template_filename):
        with open(template_filename) as tf:
            contents = tf.read()


        updated_contents = contents.replace('{{datadir}}', datadir).replace('{{mistpath}}', mistpath).replace('{{networkid}}', networkid).replace("{{genesisfile}}", genesisfile)

        with open(target_file, 'w') as nf:
            nf.write(updated_contents)


if __name__ == '__main__':
    for file in os.listdir("./templates"):
        if file.endswith(".template"):
            path = os.path.join("./templates", file)
            new_file = "./generated/{}.sh".format(file.split('.')[0])

            print("Processing file: {} => {}".format(path, new_file))
            create_sh_file(path, new_file)
