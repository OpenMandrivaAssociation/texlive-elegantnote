Name:		texlive-elegantnote
Version:	62989
Release:	1
Summary:	Elegant LaTeX Template for Notes
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/elegantnote
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/elegantnote.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/elegantnote.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
ElegantNote is designed for writing working papers, especially
for economics students. This template is based on the standard
LaTeX article class. The goal of this template is to make the
writing process easier and more comfortable.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/elegantnote
%doc %{_texmfdistdir}/doc/latex/elegantnote

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
