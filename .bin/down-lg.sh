for i in $(seq 1 1 20)
do
        echo home|proz "http://ufpr.dl.sourceforge.net/project/ubuntu-eee/Easy Peasy/1.5/easypeasy-1.5.img.iso &" 

        idCommand=$(ps -C proz | tail -1 | cut -d " " -f1)
        echo $i:$idCommand

        sleep 30

        killCommand="kill -9 "$idCommand
        echo $killCommand
        $killCommand

done
