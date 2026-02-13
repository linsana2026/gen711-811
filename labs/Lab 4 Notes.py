cd gen711-811/shell_data/untrimmed_fastq/

ls -a OR ls --all = Shwoing all hidden directories.
having a dot in front of name make a directory or file hidden.
ls. * = Wildcard.
ls -Fa = shows all directories in this format.
ls -laF = Long format.
drwxr-xr-x = red, write, and execute features.

Using the filesystem diagram below, if pwd dispalys /Users/thing, what will ls ../backup display?

1. No: there *is* a directory `backup` in `/Users`.
2. No: this is the content of `Users/thing/backup`,
  but with `..` we asked for one level further up.
3. No: see previous explanation.
  Also, we did not specify `-F` to display `/` at the end of the directory names.
4. Yes: `../backup` refers to `/Users/backup`.

ls /usr/bin/ = Shows you everythign in bin.
ls /usr/bin/*.sh = Shows specifically everything that ends in "sh".
ls /usr/bin/c* = everything starting with "c"

!1038 = Rerun that line of code from line 1038, for example.

history | grep 'grep' = Helps you find any file with 'grep' in the name, for example.
cat = prints whole file to screen.

grep TTTTT SRR097977.fastq = Shows all sequences in this file.

head or tail = top or bottom of file
-n3 = only head or tial of 3 lines.

mv  *backup.fastq backup/ = move everything to the backup folder.