# Archalien - Convert Debian packages into Arch Linux packages 

The `archalien` command-line utility allows converting Debian `.deb` packages into Arch Linux `.pkg.tar.gz` packages.

## Usage

Run the script by passing the path to the Debian package as an argument.

```bash
$ ./archalien.py <path-to-debian-package>

```

### Example

```bash
./archalien.py apt-file_2.5.4ubuntu1_all.deb
Conversion of apt-file_2.5.4ubuntu1_all.deb...

done.

The Arch Linux package:
apt-file-2.5.4ubuntu1.pkg.tar.gz

```
