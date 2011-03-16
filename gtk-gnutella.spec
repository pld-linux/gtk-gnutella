Summary:	Gnutella P2P Network Client
Summary(es.UTF-8):	Cliente de la red P2P Gnutella
Summary(pl.UTF-8):	Klient sieci Gnutella
Name:		gtk-gnutella
Version:	0.96.9
Release:	1
License:	GPL v2+
Group:		Applications/Communications
Source0:	http://downloads.sourceforge.net/gtk-gnutella/%{name}-%{version}.tar.bz2
# Source0-md5:	77e1a66685f563c668d4bbf69e4db0bb
Patch0:		%{name}-desktop.patch
URL:		http://gtk-gnutella.sourceforge.net/
BuildRequires:	bison
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel
BuildRequires:	groff
BuildRequires:	gtk+2-devel
BuildRequires:	libxml2-devel
BuildRequires:	pkgconfig
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gnutella P2P Network Client.

%description -l es.UTF-8
Cliente de la red P2P Gnutella.

%description -l pl.UTF-8
Klient sieci Gnutella.

%prep
%setup -q
%patch0 -p1

%build
./Configure \
	-Dprefix=%{_prefix} \
	-Dbindir=%{_bindir} \
	-Dprivlib=%{_datadir}/%{name} \
	-Dsysman=%{_mandir}/man1 \
	-Dldflags="-L/usr/%{_lib}" \
	-Dccflags="-Wall -I/usr/include/glib-2.0 -I/usr/%{_lib}/glib-2.0/include -I/usr/include/gtk-2.0 -I/usr/include/pango-1.0 -I/usr/%{_lib}/gtk-2.0/include -I/usr/include/atk-1.0" \
	-Dcc="%{__cc}" \
	-Doptimize="%{rpmcflags}" \
	-Dyacc="bison -y" \
	-Dgtkversion=2  \
	-Dofficial=true -ders

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	INSTALL_PREFIX=$RPM_BUILD_ROOT
%{__make} install.man \
	INSTALL_PREFIX=$RPM_BUILD_ROOT

install extra_files/%{name}.desktop $RPM_BUILD_ROOT%{_desktopdir}
install extra_files/%{name}*.png $RPM_BUILD_ROOT%{_pixmapsdir}

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README ChangeLog AUTHORS
%attr(755,root,root) %{_bindir}/gtk-gnutella
%{_datadir}/%{name}
%{_mandir}/man1/gtk-gnutella.1*
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}*.png
