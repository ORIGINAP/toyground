ls : show file in now directory.
clear : Clear console
Command History : Up/Down Arrow
AutoComplete : Tab
Show Present Time : date
AbsPath : /(root)/home/user/Document
RelativePath : ../Download(.. is go up tree) ./Download(. is now tree)
pwd : show working directory
cd : move Directory

[How to go User Home Directory?]
1. cd /home/user
2. cd
3. cd ~

[ls option]
-a : Show hidden file
-l : Show Detail
-al : Show Hidden file to Detail
-la : equal
ll : equal -alF (-F : Print file category)

mkdir : make directory
rmdir : remove directory

rmdir a b
-> remove a and b

tail -n /directory/file
head -n /directory/file
(n is print line num, default 10)
cp : copy file
mv : move file

[How can Hide file?]
add infront of filename '.'
.file
.git
.ignore

touch (file) : Modify date and time, but usually use to make 0byte file
use touch and no option flag given, file a,c,mtime change to present time

cd - : go Directory just before work.(one data saved)
grep (name) (directory) : grep string

find (directory) -name (filename) : find file in all of directory(Include child Directory)

which (command) : find command file location
which -a (command) : find command all location like root directory
whereis (command) : find command file location, source location, man file pagenum

