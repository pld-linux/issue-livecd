
%define	distversion	1.0
%define	distrelease	"%{distversion} PLD Live CD"

Summary:	PLD LiveCD release file with logo
Summary(de):	PLD LiveCD Release-Datei mit logo
Summary(pl):	Wersja PLD LiveCD z logiem
Name:		issue-livecd
Version:	%{distversion}
Release:	1
License:	GPL
Group:		Base
Provides:	issue
Obsoletes:	issue
Obsoletes:	issue-alpha
Obsoletes:	issue-fancy
Obsoletes:	issue-logo
Obsoletes:	issue-pure
Obsoletes:	mandrake-release
Obsoletes:	redhat-release
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PLD LiveCD release file with logo.

%description -l de
PLD LiveCD Release-Datei mit logo.

%description -l pl
Wersja PLD LiveCD z logiem.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}

cat > $RPM_BUILD_ROOT%{_sysconfdir}/issue <<EOF
  _
 / )     PLD Live CD %{distversion} \m, \r
/ /       Welcome to \n
 ( -.      Login as root || user
 \\\\   \\\\      \u user(s)
  \\\\  \\\\\\\\
   \\\`| \\\\\\\\
    |  \\\`
    |

EOF
echo -ne "\l " >> $RPM_BUILD_ROOT%{_sysconfdir}/issue

cat > $RPM_BUILD_ROOT%{_sysconfdir}/issue.net <<EOF
  _
 / )     PLD Live CD %{distversion} %m, %r
/ /       Welcome to %h
 ( -.
 \\\\   \\\\
  \\\\  \\\\\\\\
   \\\`| \\\\\\\\
    |  \\\`
    |

EOF
echo %{distrelease} > $RPM_BUILD_ROOT%{_sysconfdir}/pld-release

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_sysconfdir}/pld-release
%config(noreplace) %{_sysconfdir}/issue*
