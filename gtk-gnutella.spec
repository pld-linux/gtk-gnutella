Summary:	Gnutella P2P Network Client
Summary(es):	Cliente de la red P2P Gnutella
Summary(pl):	Klient sieci Gnutella
Name:		gtk-gnutella
Version:	0.93.4
Release:	1
License:	GPL
Group:		Applications/Communications
Source0:	http://dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.bz2
# Source0-md5:	d7eac5792b01694ddcb5969030ec9bbb
URL:		http://gtk-gnutella.sourceforge.net/
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel
BuildRequires:	libxml2-devel
BuildRequires:	zlib-devel
BuildRequires:	bison
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gnutella P2P Network Client.

%description -l es
Cliente de la red P2P Gnutella.

%description -l pl
Klient sieci Gnutella.

%prep
%setup -q

%build
./Configure -Dprefix=%{_prefix} -Dbindir=%{_bindir} \
	-Dprivlib=%{_datadir}/%{name} \
	-Dsysman=%{_mandir}/man1 -Dccflags="-Wall" -Dcc=%{__cc} \
	-Doptimize="%{rpmcflags}" -Dyacc="bison -y" -Dgtkversion=2  \
	-Dofficial=true -ders

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install INSTALL_PREFIX=$RPM_BUILD_ROOT
%{__make} install.man INSTALL_PREFIX=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README ChangeLog AUTHORS
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man1/*
