Name:     ocaml-inotify

Version:  2.3
Release:  1
Summary:  OCaml bindings for inotify
License:  GPLv2+
URL:      https://github.com/whitequark/ocaml-inotify
Source0:  https://github.com/whitequark/ocaml-inotify/archive/v%{version}.tar.gz

BuildRequires: ocaml
BuildRequires: ocaml-findlib
BuildRequires: inotify-tools-devel
Requires:      inotify-tools

%prep
%setup -q

%build
./configure \
   --prefix=%{_prefix} \
make all

%install
export DESTDIR=%{buildroot}
export OCAMLFIND_DESTDIR=%{buildroot}$(ocamlfind printconf destdir)
export DLLDIR=$OCAMLFIND_DESTDIR/stublibs

install -d $OCAMLFIND_DESTDIR/%{ocamlpck}
install -d $OCAMLFIND_DESTDIR/stublibs
make install

%files
/usr/lib64/ocaml/inotify/META
/usr/lib64/ocaml/inotify/inotify.a
/usr/lib64/ocaml/inotify/inotify.cma
/usr/lib64/ocaml/inotify/inotify.cmi
/usr/lib64/ocaml/inotify/inotify.cmxa
/usr/lib64/ocaml/inotify/inotify.mli
/usr/lib64/ocaml/inotify/inotify.cmx

%description
OCAML bindings for inotify
