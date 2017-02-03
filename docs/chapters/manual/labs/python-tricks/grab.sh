
if test -z "$1"
then
    echo "Supply a name or single word description of file"
    exit 1
else
    filename=$1
fi

f_xwd=/tmp/$filename.xwd
f_png=/tmp/$filename.png

### Use alt-tab to get a clear view of the window to click on 
xwd -nobdrs -out $f_xwd

###
convert $f_xwd $f_png

echo $f_png


echo "Adjust $f_png in Gimp? Y/n"
read usegimp

if [ "$usegimp"  == "y" ] || [ "$usegimp" == "Y" ]; 
then 
    gimp $f_png
else
    exit 0
fi

 
