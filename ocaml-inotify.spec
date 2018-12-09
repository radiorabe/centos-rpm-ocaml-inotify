Name:     ocaml-inotify
Version:  2.3
Release:  1
Summary:  OCaml bindings for inotify

%global libname %(echo %{name} | sed -e 's/^ocaml-//')

License:  GPLv2+
URL:      https://github.com/whitequark/ocaml-inotify
Source0:  https://github.com/whitequark/ocaml-inotify/archive/v%{version}.tar.gz#/%{name}-${version}.tar.gz

BuildRequires: ocaml
BuildRequires: ocaml-findlib
BuildRequires: ocaml-ocamlbuild
BuildRequires: ocaml-ocamldoc
BuildRequires: ocaml-lwt-devel
BuildRequires: inotify-tools-devel
BuildRequires: ocaml-lwt
Requires:      inotify-tools


%description
OCAML bindings for inotify


%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature
files for developing applications that use %{name}.


%prep
%autosetup -n %{name}-%{version}

%build
./configure \
   --prefix=%{_prefix} \
   --docdir=%{buildroot}/%{_libdir}/ocaml/doc/%{libname}
make all

%install
export DESTDIR=%{buildroot}
export OCAMLFIND_DESTDIR=%{buildroot}$(ocamlfind printconf destdir)
export DLLDIR=$OCAMLFIND_DESTDIR/stublibs
export DOCDIR=$OCAMLFIND_DESTDIR/doc/%{libname}

install -d $OCAMLFIND_DESTDIR/%{ocamlpck}
install -d $OCAMLFIND_DESTDIR/stublibs
make install

%files
%doc README.md
%doc %{_libdir}/ocaml/doc/%{libname}
%license LICENSE.txt
%{_libdir}/ocaml/%{libname}
%{_libdir}/ocaml/stublibs/dll%{libname}_stubs.so
%{_libdir}/ocaml/stublibs/dll%{libname}_stubs.so.owner
%ifarch %{ocaml_native_compiler}
%exclude %{_libdir}/ocaml/%{libname}/*.a
%exclude %{_libdir}/ocaml/%{libname}/*.cmxa
%exclude %{_libdir}/ocaml/%{libname}/*.cmx
%exclude %{_libdir}/ocaml/%{libname}/*.mli
%endif

%files devel
%license LICENSE.txt
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/%{libname}/*.a
%{_libdir}/ocaml/%{libname}/*.cmxa
%{_libdir}/ocaml/%{libname}/*.cmx
%{_libdir}/ocaml/%{libname}/*.mli
%endif

%changelog
* Sun Dec  9 2018 Lucas Bickel <hairmare@rabe.ch> - 0.7.1-0.1
- Initialize RPM changelog
- Cleanup and add separate -devel subpackage
