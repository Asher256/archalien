# Archalien - Convert Debian packages into Arch Linux packages 

The [archalien](https://github.com/Asher256/archalien) command-line utility allows converting Debian `.deb` packages into Arch Linux `.pkg.tar.gz` packages.

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

## License

Copyright (c) [Asher256](http://asher256.com/)

This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with This program; if not, write to the Free Software Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
