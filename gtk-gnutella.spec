Summary:	Gnutella P2P Network Client
Summary(pl):	Klient sieci Gnutella
Name:		gtk-gnutella
Version:	0.92.1c
Release:	1
License:	GPL
Group:		Applications/Communications
Source0:	http://cesnet.dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.bz2
# Source0-md5:	d20ef03a5474aa0d961c52030caf206b
#Source0:	http://dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.bz2
Patch0:		%{name}-gtk2.patch
URL:		http://gtk-gnutella.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gnutella P2P Network Client.

%description -l pl
Klient sieci Gnutella.

%prep
%setup -q
#%patch0 -p1

%build
rm -f missing
%{__gettextize}
mv configure.in~ configure.in
%{__libtoolize}
%{__aclocal}
%{__automake}
%{__autoconf}
%configure --enable-gtk2
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README ChangeLog NEWS AUTHORS
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
