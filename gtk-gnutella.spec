Summary:	Gnutella P2P Network Client
Summary(pl):	Klient sieci Gnutella
Name:		gtk-gnutella
Version:	0.91
Release:	1
License:	GPL
Group:		Applications/Communications
Source0:	http://telia.dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.gz
URL:		http://gtk-gnutella.sourceforge.net
BuildRequires:	gtk+-devel
BuildRequires:	libxml2-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _prefix         /usr/X11R6

%description
Gnutella P2P Network Client.

%description -l pl
Klient sieci Gnutella.

%prep
%setup -q

%build
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog NEWS AUTHORS
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
