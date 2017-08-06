% Latex style for dissertations (Departamento de Informatica, Universidade de Evora)
% Versão 1.5
%
% With the contributes of fc, jsaias, tcg, dmendes, ... well, almost everyone @di.uevora.pt
%
%	Free as in freedom
%


\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{teseue}[
	2015/02/05 --- 
	Estilo para dissertacoes da Universidade de Evora, versao 2.0 RC ---
	Com o contributo de fc, jsaias, tcg, dmendes e quase todos @di.uevora.pt --- 
	Codigo Livre 
]
% Language adjustment

% Hyperref adjustments
% \RequirePackage{hyperref}
% \hypersetup{
% 	colorlinks=true,
% 	%pdfstartview=FitV,
% 	%pdfpagelabels=true,
% 	linkcolor=[rgb]{0.4 0.1 0.1},
% 	citecolor=[rgb]{0.1 0.4 0.1},
% 	urlcolor=[rgb]{0.1 0.1 0.4}
% }

% Document adjustment
\LoadClass[11pt,a4paper]{book}
\RequirePackage[top=3cm, bottom=3cm, left=2cm, right=2cm]{geometry} 
\RequirePackage{setspace} % for spacing environment
\RequirePackage{etoolbox} % for advanced authoring
\RequirePackage{graphicx}
\RequirePackage{acronym}
\RequirePackage{tikz}
\RequirePackage{makeidx}
\RequirePackage{fontspec}
\RequirePackage{array} % para alinhar verticalmente as linhas das tabelas (na lombada)
\setmainfont{Source Sans Pro}[
	UprightFont = {* Light},
	ItalicFont = {* Light Italic},
	BoldFont = {*}
]
%
\newfontfamily\xlightfont{Source Sans Pro}[
	UprightFont = {* ExtraLight},
	ItalicFont = {* ExtraLight Italic},
	BoldFont = {* Light}
]
%\newfontfamily\lightfont{Source Sans Pro}[UprightFont = {* Light}]
%\RequirePackage[rgb]{xcolor}
\definecolor{uered}{RGB}{158 27 50}
\definecolor{uegray}{RGB}{88 89 91}
\definecolor{uegrey}{RGB}{88 89 91}
\definecolor{ueblack}{RGB}{0 0 0}

% Paragraph ajustement
\setlength{\parindent}{0mm}
\setlength{\parskip}{3mm}
\renewcommand{\baselinestretch}{1.0} % 1.5 for double-space

%
%\RequirePackage{anyfontsize}

%%%%%%%%%%%%%%%%%%
% Style definition
%%%%%%%%%%%%%%%%%%
\newcommand{\@Monografia}{Disserta\c{c}\~{a}o}
\newcommand{\@monografia}{disserta\c{c}\~{a}o}


\DeclareOption{doutoramento}{
	\newcommand{\@Grau}{Doutor}
	\newcommand{\@grau}{doutor}
}
\DeclareOption{mestrado}{
	\newcommand{\@Grau}{Mestre}
	\newcommand{\@grau}{mestre}
}
%
%	Os azulejos da capa determinam a area cientifica (e vice-versa)
%
\newcommand{\@AZULEJOS}{rascunhocet.jpg}
\DeclareOption{ct}{
	\renewcommand{\@AZULEJOS}{capacet.jpg}
}
\DeclareOption{csh}{
	\renewcommand{\@AZULEJOS}{capacsh.jpg}
}
\DeclareOption{artes}{
	\renewcommand{\@AZULEJOS}{capaart.jpg}
}
\DeclareOption{ctR}{
	\renewcommand{\@AZULEJOS}{rascunhocet.jpg}
}
\DeclareOption{cshR}{
	\renewcommand{\@AZULEJOS}{rascunhocsh.jpg}
}
\DeclareOption{artesR}{
	\renewcommand{\@AZULEJOS}{rascunhoart.jpg}
}
%
\DeclareOption*{\PassOptionsToClass{\CurrentOption}{book}}
\ProcessOptions
%
% ----------------------------------------------------------------
%
\renewcommand{\familydefault}{\sfdefault}
%
%
% ================================================================
%
%	INTERFACE PUBLICO
%
% ================================================================
%
%% Titulo
%
\newcommand{\@TITULO}{T\'{i}tulo da tese}
\newcommand{\@TITLE}{Thesis title}
\DeclareRobustCommand{\tueTITULO}[2]{%
	\renewcommand{\@TITULO}{#1}
	\renewcommand{\@TITLE}{#2}
}
%
%% Subtitulo
%
\providebool{@comSubtitulo}
\newcommand{\@SUBTITULO}{Subt\'{i}tulo da tese}
\newcommand{\@SUBTITLE}{Thesis subtitle}
\DeclareRobustCommand{\tueSUBTITULO}[2]{%
	\renewcommand{\@SUBTITULO}{#1}
	\renewcommand{\@SUBTITLE}{#2}
	\booltrue{@comSubtitulo}
}
%
%% Candidato
%
\newcommand{\@CANDIDATO}{Nome do candidato}
\DeclareRobustCommand{\tueCANDIDATO}[1]{%
	\renewcommand{\@CANDIDATO}{#1}
}
%
%% Curso
%
\newcommand{\@CURSO}{Curso}
\DeclareRobustCommand{\tueCURSO}[1]{%
	\renewcommand{\@CURSO}{#1}
}
%
%% Especialidade
%
\providebool{@comEspecialidade}
\boolfalse{@comEspecialidade}
\newcommand{\@ESPECIALIDADE}{ND}
\DeclareRobustCommand{\tueESPECIALIDADE}[1]{%
	\renewcommand{\@ESPECIALIDADE}{#1}
	\booltrue{@comEspecialidade}
}
%
%% Orientador ou Orientadora
%
\newcommand{\@MFORIENTADOR}{Orientador}
\newcommand{\@NOMEORIENTADOR}{Nome do/a orientador/a}
\DeclareRobustCommand{\tueORIENTADOR}[2]{%
	\renewcommand{\@MFORIENTADOR}{#1}
	\renewcommand{\@NOMEORIENTADOR}{#2}
}
%
%% CoOrientador ou CoOrientadora
%
\providebool{@comSegOrientador}
\boolfalse{@comSegOrientador}
\newcommand{\@MFSEGORIENTADOR}{ND}
\newcommand{\@NOMESEGORIENTADOR}{ND}
\DeclareRobustCommand{\tueSEGUNDOORIENTADOR}[2]{%
	\renewcommand{\@MFSEGORIENTADOR}{#1}
	\booltrue{@comSegOrientador}
	\renewcommand{\@NOMESEGORIENTADOR}{#2}
}
%
%% Terceiro Orientador ou Orientadora
%
\providebool{@comTerOrientador}
\boolfalse{@comTerOrientador}
\newcommand{\@MFTERORIENTADOR}{ND}
\newcommand{\@NOMETERORIENTADOR}{ND}
\DeclareRobustCommand{\tueTERCEIROORIENTADOR}[2]{%
	\renewcommand{\@MFTERORIENTADOR}{#1}
	\booltrue{@comTerOrientador}
	\renewcommand{\@NOMETERORIENTADOR}{#2}
}
%
%% Departamento
%
\newcommand{\@DEPARTAMENTO}{Departamento}
\DeclareRobustCommand{\tueDEPARTAMENTO}[1]{%
	\renewcommand{\@DEPARTAMENTO}{#1}
}
%
%% Escola
%
\newcommand{\@ESCOLA}{Escola}
\DeclareRobustCommand{\tueESCOLA}[1]{%
	\renewcommand{\@ESCOLA}{#1}
}
%
%% Data
%
\newcommand{\@DATA}{Data}
\DeclareRobustCommand{\tueDATA}[1]{%
	\renewcommand{\@DATA}{#1}
}
%
%% Palavras chave
%
\newcommand{\@PALAVRASCHAVE}{palavra chave 1, palavra chave 2, palavra chave 3, palavra chave 4, palavra chave 5}
\newcommand{\@KEYWORDS}{keyword 1, keyword 2, keyword 3, keyword 4, keyword 5}
\DeclareRobustCommand{\tuePALAVRASCHAVE}[2]{%
	\renewcommand{\@PALAVRASCHAVE}{#1}
	\renewcommand{\@KEYWORDS}{#2}
}
%
%% Dedicatoria
%
\newcommand{\@DEDICATORIA}{Dedicat\'{o}ria}
\DeclareRobustCommand{\tueDEDICATORIA}[1]{%
	\renewcommand{\@DEDICATORIA}{#1}
}
%
%% Preambulo
%
\newcommand{\@PREAMBULOLATEX}{\makeindex}
\DeclareRobustCommand{\tuePREAMBULOLATEX}[1]{%
	\renewcommand{\@PREAMBULOLATEX}{#1}
}
%
%% Prefacio
%
\newcommand{\@PREAMBULO}{	
	% \include{prefacio}
	\include{agradecimentos}
	\@TABELAS
	\include{sumario}
	\include{abstract}
}
\DeclareRobustCommand{\tuePREAMBULO}[1]{%
	\renewcommand{\@PREAMBULO}{#1}
}
%
%% Conteudo
%
\newcommand{\@CONTEUDO}{}
\DeclareRobustCommand{\tueCONTEUDO}[1]{%
	\renewcommand{\@CONTEUDO}{#1}
}
%
%% Apendices
%
\newcommand{\@APENDICES}{}
\DeclareRobustCommand{\tueAPENDICES}[1]{%
	\renewcommand{\@APENDICES}{#1}
}
%
%% Bibliografia
%
\newcommand{\@BIBLIOGRAFIA}{
	%	Incluir todas as entradas na bibliografia
	\nocite{*}
	%	Estilo das citações
	\bibliographystyle{alpha}
	%	Lista das referências
	\bibliography{bibliografia}
}
\DeclareRobustCommand{\tueBIBLIOGRAFIA}[1]{%
	\renewcommand{\@BIBLIOGRAFIA}{#1}
}
%
%% Indice remissivo
%
\newcommand{\@INDICEREMISSIVO}{
	\cleardoublepage 
	\printindex
}
\DeclareRobustCommand{\tueINDICEREMISSIVO}[1]{%
	\renewcommand{\@INDICEREMISSIVO}{#1}
}
%
%% DISSERTACAO
%
\DeclareRobustCommand{\tueDOCUMENTO}{
	% \usepackage[portuguese]{babel}
	\@PREAMBULOLATEX
	\begin{document}
		\frontmatter
		% \@CAPA
		\@SUBCAPA
		\@SUBCAPA
		\@PAGINADEDICATORIA
		\@PREAMBULO
		\mainmatter
		\@CONTEUDO
		\appendix
		\@APENDICES
		\backmatter
		\@BIBLIOGRAFIA
		\@INDICEREMISSIVO
		\@CONTRACAPA
	\end{document}
}
%
%% CAPA E SUBCAPA
%
\DeclareRobustCommand{\tueCAPAS}{
	\usepackage[portuguese]{babel}
	\@PREAMBULOLATEX
	\begin{document}
		\frontmatter
		\@CAPA
		\@SUBCAPA
		\@CONTRACAPA
		\@LOMBADA
	\end{document}
}
%
%
% ================================================================
%
%	Identificacao do documento
%
% ================================================================
%
%% Sumario/Resumo
%
\newenvironment{tueSUMARIO}{
	\chapter*{Sumário}\addcontentsline{toc}{chapter}{Sumário}
    {\Large Data Mining Educacional Aplicado aos Dados do Moodle da Universidade de Évora}
    \bigskip
}{
	\par
	\bigskip
	\textbf{Palavras chave:}~\@PALAVRASCHAVE
}
%
%% Abstract
%
\newenvironment{tueABSTRACT}{
	\chapter*{Abstract}\addcontentsline{toc}{chapter}{Abstract}
	\begin{center}
		\huge
		\textbf{\@TITLE}
			\par
			\Large
		\ifbool{@comSubtitulo}{
			\@SUBTITLE
		}{
			\phantom{FILL}
		}
	\end{center}
}{
	\par
	\bigskip
	\textbf{Keywords:}~\@KEYWORDS
}
%
%% Abstract
%
\newenvironment{tueACRONIMOS}{
	\chapter*{List of Acronyms}\addcontentsline{toc}{chapter}{List of Acronyms}
}{
}
%
% ================================================================
%
%	Tabela de conteudos
%
% ================================================================
%
\newcommand{\@TABELAS}{	
	\begin{spacing}{.5}
		%
		\@blankoddpage
		\cleardoublepage
		\tableofcontents
		\addcontentsline{toc}{chapter}{Contents}
		%
		\@blankoddpage
		\cleardoublepage
		\listoffigures
		\addcontentsline{toc}{chapter}{List of Figures}
		%
		\@blankoddpage
		\cleardoublepage
		\listoftables
		\addcontentsline{toc}{chapter}{List of Tables}
		%
		\@blankoddpage
		\cleardoublepage
		\include{acronimos}
	\end{spacing}
}
\DeclareRobustCommand{\tueTABELAS}[1]{
	\renewcommand{\@TABELAS}{#1}
}
%
% ================================================================
%
%	DEFINICOES PRIVADAS
%
% ================================================================
%
%
% ================================================================
%
%	CAPA
%
% ================================================================
%
\DeclareRobustCommand{\@CAPA}{   % v.2013: capa uniforme, jsaias
	\thispagestyle{empty}
		\vspace*{-2.1cm}
		\begin{flushright}
			\includegraphics[width=6cm]{teseue-logo.pdf}
			\par
			%
			\vspace{1em}		
			%
			{\Huge \textbf{\@TITULO}}
			%
			\par		
			%
			{\LARGE \@SUBTITULO}
			%
			\par
			%
			\rule{\textwidth}{1pt}
			%
			\par
			\vspace{1em}
			%
			{\Large \textit{\@CANDIDATO}}
			%
			\par
			\vspace{3em}		
			%
			{Tese apresentada \`{a} Universidade de \'{E}vora}\\
			{para obten\c{c}\~{a}o do Grau de \@Grau\ em \@CURSO}\\
			\ifbool{@comEspecialidade}{
				{na especialidade \@ESPECIALIDADE}\\
			}{~\\}
			%
			\par
			\vspace{2em}	
			%
			%	Orientacao
			%
			\begin{tabular}{rr}%
				\@MFORIENTADOR & \textit{\@NOMEORIENTADOR}\\%
				\ifbool{@comSegOrientador}{%
					\@MFSEGORIENTADOR & \textit{\@NOMESEGORIENTADOR}\\%				
					\ifbool{@comTerOrientador}%
						{\@MFTERORIENTADOR & \textit{\@NOMETERORIENTADOR}\\}%
						{\\}%
				}{~ \\ ~ \\}%
			\end{tabular}%
			%
			\par%
			\vspace{2em}
			%	
			\textit{Esta \@monografia\ inclui as cr\'{i}ticas e sugest\~{o}es feitas pelo J\'{u}ri}
			%
			\par
			\vspace{2em}
			%
			{\@DATA}
			%
			\par
			\vspace{2em}
			%
			\begin{centering}
			    %\includegraphics[trim=0.89cm 0cm 0.38cm 0cm, clip, width=\textwidth]{\@AZULEJOS}
			    \includegraphics[width=\linewidth]{\@AZULEJOS}
			\end{centering}
			%
			\par
			\vspace{2em}
			%
			{ESCOLA DE CIÊNCIAS E TECNOLOGIA - DEPARTAMENTO DE INFORMÁTICA}
			%
		\end{flushright}
% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
	\newpage\hspace{1mm}\thispagestyle{empty}
	\cleardoublepage
}
%
% ================================================================
%
%	Segunda pagina de rosto
%
% ================================================================
%
\DeclareRobustCommand{\@SUBCAPA}{   % v.2013: capa uniforme, jsaias
	\thispagestyle{empty}
	%\vspace*{-0.8cm}
	\begin{tabular}{lcr}
		%
		% pomba
		%
	    \vspace*{-1.5cm}\parbox[t][\textheight][t]{2.63cm}{\includegraphics[width=8em]{teseue-pomba} \\ } 
	    & 
	    %
	    % tracejado vertical a esquerda
	    %
	    \hspace{1em}
	  	\parbox[t][\textheight][t]{0.4cm}{
	  		\vspace*{-3.2cm}
	  		\begin{tikzpicture}
	  			\foreach \y in {1, ..., 42} {
	  				\fill[fill=uegrey] (0,\y*0.55) circle (0.05cm);
	  			}
	  		\end{tikzpicture}
	  	}
	  	& 
	  	%
	  	%	resumo
	  	%
	    \vspace*{-1.5cm}
	    \parbox[t][0.9\textheight][t]{10.1cm}{
	    	%
			\vspace{-2.8cm} % recuo vertical igual ao comprimento da imagem
			%
			{\Large \textbf{{\color{uered} UNIVERSIDADE DE ÉVORA}}}\\
			%
			\par
			%
			{\large \textbf{\@ESCOLA}} \\
			%
			\par
			%
			{\large \@DEPARTAMENTO} \\
			%
			\par
			\vspace*{12em}
			%
			{\Large \textbf{\@TITULO}} \\
			%
			\par			%
			\vspace{2em}
			%
			{\large \textbf{\@CANDIDATO}}\\
			%
			\par			%
			\vspace{4em}
			%
			%	Orientacao
			%
			\begin{tabular}{rl}%
				Orienta\c{c}\~{a}o & \textit{\@NOMEORIENTADOR}\\%
				\ifbool{@comSegOrientador}{%
					& \textit{\@NOMESEGORIENTADOR}\\%				
					\ifbool{@comTerOrientador}%
						{& \textit{\@NOMETERORIENTADOR}\\}%
						{\\}%
				}{~ \\ ~ \\}%
			\end{tabular}%
			%
			\par
			\vspace{4em}
			%
			% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
			%
			{\large \textbf{\@CURSO}}
			%
			\par
			\vspace{2em}
			%
			{\normalsize \@Monografia}
			%
			\par
			\vspace{6em}
			%
			{\small \@DATA}
			%
			\par
			\vspace*{3em}
			%
			{\footnotesize\textit{Esta \@monografia\ inclui as cr\'{i}ticas e sugest\~{o}es feitas pelo J\'{u}ri}\\}
			%
		}
	\end{tabular} 
	% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
	\newpage\hspace{1mm}\thispagestyle{empty}
	\cleardoublepage
}
%
% ================================================================
%
%	Contracapa
%
% ================================================================
%
\DeclareRobustCommand{\@CONTRACAPA}{
	\cleardoublepage
	\newpage
	\thispagestyle{empty}
	% mancha no fundo
	~
	\vfill
	% mancha a direita
	\begin{flushright}
		\includegraphics[width=0.5\textwidth]{teseue-logo-iifa}\\
		%
		\par
		\vspace{1em}
		%
		\begingroup
			\color{uegray}
			\textbf{Contactos:}\\
			Universidade de \'{E}vora\\
			\textbf{Escola de Ciências e Tecnologia - Departamento de Informática}\\
			Pal\'{a}cio do Vimioso~|~Largo Marqu\^{e}s de Marialva, Apart.\ 94\\
			7002 - 554 \'{E}vora~|~Portugal\\
			Tel: (+351)~266~706~581\\
			Fax: (+351)~266~744~677\\
			email: iifa@uevora.pt\\
		\endgroup
	\end{flushright}
}
%
% ================================================================
%
%	Lombada
%
% ================================================================
%
\DeclareRobustCommand{\@LOMBADA}{
	\newpage
	\thispagestyle{empty}
	\newgeometry{left=1mm,right=1mm,top=1mm,bottom=1mm}
	\centering
	\rotatebox{90}{
		\begin{tabular}{m{5mm}m{120mm}m{100mm}m{45mm}}
			~
			&
			{\large\bf\@TITULO}
			&
			\begin{minipage}{90mm}
				\centering\large\em\@CANDIDATO
			\end{minipage}
			&
			{\includegraphics[height = 2em]{teseue-logo-iifa}}
		\end{tabular}
	}
}
%
% ================================================================
%
%	Dedicatoria
%
% ================================================================
%
\DeclareRobustCommand{\@PAGINADEDICATORIA}{
	\@blankoddpage
	\thispagestyle{empty}
	\begin{flushright}
		\ \\
		\vspace{5cm}
		\it \@DEDICATORIA
	\end{flushright}
	\@blankoddpage
}
%
% ================================================================
%
%	Apendice
%
% ================================================================
%
\newcommand{\theappendix}{
	\renewcommand{\chaptername}{Annexes}
	\@blankoddpage
	\thispagestyle{empty}
	\vspace*{7cm}
	\begin{center}
	{\bf \Huge Annexes}
	\end{center}
	\vfill
}
%
% ================================================================
%
%	Cabecalho vazio para paginas pares no fim dos capitulos (tcg!)
%
% ================================================================
%
\def\blankpage{\pagestyle{empty}\cleardoublepage\pagestyle{headings}}
\newcommand{\@blankoddpage}{
	\if@openright
		\clearpage
		\blankpage
	\else
		\clearpage
	\fi
}
%
% ================================================================
%
%	Estilo para as seccoes
%
% ================================================================
%
\renewcommand{\section}{\@startsection
	{section}%                   % the name
	{1}%                         % the level
	{0mm}%                       % the indent
	{-\baselineskip}%            % the before skip
	{0.5\baselineskip}%          % the after skip
	{\normalfont\Large\bfseries}	% the style
}
%
% ================================================================
%
% Estilos para capitulos
%
% ================================================================
%
% ----------------------------------------------------------------
% Geral
% ----------------------------------------------------------------
\renewcommand\chapter{%
	\@blankoddpage
	\thispagestyle{plain}
	\global\@topnum\z@
	\@afterindentfalse
	\secdef\@chapter\@schapter
}
% ----------------------------------------------------------------
% Capitulo numerado
% ----------------------------------------------------------------
\renewcommand{\@makechapterhead}[1]{
	\@blankoddpage
	\vspace*{100\p@}
  	\begingroup
		\parindent
		\z@
		\raggedright
		%\normalfont
		\vspace{5pt}
		%\hrule 
		%
		%	Chapter Number
		%
		\ifnum \c@secnumdepth >\m@ne
			%\bf \Huge \chaptername\space \thechapter	% Chapter number
			\begin{flushright}
				{\fontsize{256}{307}\selectfont \color{uegray} \thechapter}
			\end{flushright}
			%\par\nobreak
			%\vskip 20\p@
			\vspace{.75cm}
			%\\
		\fi
		%
		%	Chapter title
		%
		\begin{flushright}
			{\fontsize{32}{38}\selectfont \color{uegray} #1}
		\end{flushright}		
		%\par
		\vspace{5pt}
		%\hrule
		\nobreak
		\vskip 40\p@
	\endgroup
}
% ----------------------------------------------------------------
% Capitulo nao numerado
% ----------------------------------------------------------------
\renewcommand{\@makeschapterhead}[1]{
	\@blankoddpage
	\vspace*{100\p@}
	\begingroup
		\parindent
		\z@
		\raggedright
		\vspace{5pt}
		\interlinepenalty\@M
		%
		%	Chapter title
		%
		\begin{flushright}
			{\fontsize{32}{38}\selectfont \color{uegray} #1}
		\end{flushright}
		\vspace{5pt}
		\nobreak
		\vskip 40\p@
	\endgroup
}
%
%
%
%
%
% \endinput
