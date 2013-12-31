
%define	distversion	1.0
%define	distrelease	"%{distversion} PLD Live CD"

Summary:	PLD LiveCD release file with logo
Summary(de.UTF-8):	PLD LiveCD Release-Datei mit logo
Summary(pl.UTF-8):	Wersja PLD LiveCD z logiem
Name:		issue-livecd
Version:	%{distversion}
Release:	3
License:	GPL
Group:		Base
Provides:	issue
Obsoletes:	issue
Obsoletes:	issue-alpha
Obsoletes:	issue-fancy
Obsoletes:	issue-logo
Obsoletes:	issue-pure
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PLD LiveCD release file with logo.

%description -l de.UTF-8
PLD LiveCD Release-Datei mit logo.

%description -l pl.UTF-8
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

# CPE_NAME = cpe:/ {part} : {vendor} : {product} : {version} : {update} : {edition} : {language}
# http://cpe.mitre.org/specification/
cat >$RPM_BUILD_ROOT%{_sysconfdir}/os-release <<EOF
NAME="PLD Linux"
VERSION="%{distversion} (%{distname})"
ID="pld"
VERSION_ID="%{distversion}"
PRETTY_NAME="PLD Linux %{distversion} (%{distname})"
ANSI_COLOR="0;32"
CPE_NAME="cpe:/o:pld-linux:pld:%{distversion}"
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_sysconfdir}/os-release
%{_sysconfdir}/pld-release
%config(noreplace) %{_sysconfdir}/issue*
