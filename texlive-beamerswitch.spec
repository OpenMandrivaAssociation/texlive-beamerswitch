Name:		texlive-beamerswitch
Version:	64182
Release:	1
Summary:	Convenient mode selection in Beamer documents
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/beamerswitch
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/beamerswitch.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/beamerswitch.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/beamerswitch.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This class is a wrapper around the beamer class to make it
easier to use the same document to generate the different forms
of the presentation: the slides themselves, an abbreviated
slide set for transparencies or online reference, an n-up
handout version (various layouts are provided), and a
transcript or set of notes using the article class. The class
provides a variety of handout layouts, and allows the mode to
be chosen from the command line (without changing the document
itself).

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/beamerswitch
%{_texmfdistdir}/tex/latex/beamerswitch
%doc %{_texmfdistdir}/doc/latex/beamerswitch

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
