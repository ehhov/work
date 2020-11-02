#include <stdio.h>

struct book {
	char *a;
	char *t;
	char *l;
};

void print_book_html(FILE *stream, struct book item, int last);
void print_field_html(FILE *stream, const char *field, const struct book *books, int len, int last);
void print_book_plain(FILE *stream, struct book item, int last);
void print_field_plain(FILE *stream, const char *field, const struct book *books, int len, int last);
void print_to_file(const char *filename, void (*printer)(FILE *stream, const char *field, const struct book *books, int len, int last));

static const char *plainfile = "books";
static const char *htmlfile = "books.html";
void (*print_book)(FILE *, struct book, int) = print_book_html;
static const struct book math[] = {
	{ "Э. Леман", "Проверка статистических гипотез", "https://google.com" },
	{ "Рубаков, Исаев", "Теория групп и симметрий", "https://it.b-ok2.org/book/2871128/bf72ea" },
};
static const struct book physics[] = {
	{ "Г. Голдстейн", "Классическая механика", "http://www.imash.ru/netcat_files/file/BIBLIO/sopromat/%D0%93%D0%BE%D0%BB%D0%B4%D1%81%D1%82%D0%B5%D0%B9%D0%BD%20%D0%93_%20-%20%D0%9A%D0%BB%D0%B0%D1%81%D1%81%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B0%D1%8F%20%D0%BC%D0%B5%D1%85%D0%B0%D0%BD%D0%B8%D0%BA%D0%B0%20-%201957.pdf" },
	{ "П. Рамон", "Теория поля. Современный вводный курс", "http://booksshare.net/index.php?id1=4&category=physics&author=ramon-p&book=1984" },
	{ "Пескин, Шредер", "Введение в квантовую теорию поля", "http://nuclphys.sinp.msu.ru/books/b/%D0%9F%D0%B5%D1%81%D0%BA%D0%B8%D0%BD_%D0%A8%D1%80%D0%B5%D0%B4%D0%B5%D1%80.htm" },
	{ "Славнов, Фаддеев", "Введение в квантовую теорию калибровочных полей", "http://nuclphys.sinp.msu.ru/books/b/%D0%A1%D0%BB%D0%B0%D0%B2%D0%BD%D0%BE%D0%B2_%D0%A4%D0%B0%D0%B4%D0%B4%D0%B5%D0%B5%D0%B2.htm" },
	{ "Л. Райдер", "Квантовая теория поля", "http://nuclphys.sinp.msu.ru/books/b/rajder.htm" },
	{ "Боголюбов, Ширков", "Введение в теорию квантовых полей", "http://nuclphys.sinp.msu.ru/books/b/%D0%91%D0%BE%D0%B3%D0%BE%D0%BB%D1%8E%D0%B1%D0%BE%D0%B2_%D0%A8%D0%B8%D1%80%D0%BA%D0%BE%D0%B2_1984.htm" },
	{ "Боголюбов, Ширков", "Квантовые поля", "http://nuclphys.sinp.msu.ru/books/b/bogolyubov_shirkov.htm" },
	{ "Б.С. Ишханов, И.М. Капитонов, Н.П. Юдин", "Частицы и атомные ядра", "http://nuclphys.sinp.msu.ru/books/b/ikyu.htm" },
};
static const struct book english[] = {
	{ "Коваленко И.Ю., Сафонова М.А.", "Effective reading, speaking, writing for senior science students", "https://el.b-ok2.org/book/3589719/b3e555" },
};

void
print_book_html(FILE *stream, struct book item, int last)
{
	fprintf(stream, "\t<li>\n");
	fprintf(stream, "\t%s, \"%s\".\n", item.a, item.t);
	fprintf(stream, "\t<a href=\"https://www.google.com/search?&q=%s, %s\">Google search</a> | ", item.a, item.t);
	fprintf(stream, "\t<a href=\"%s\">link</a>\n", item.l);
	fprintf(stream, "\t</li>\n");
	if (!last)
		fprintf(stream, "\n");
}

void
print_field_html(FILE *stream, const char *field, const struct book *books, int len, int last)
{
	int i;
	fprintf(stream, "<h1>%s</h1>\n<ol>\n", field);
	for (i = 0; i < len; i++)
		print_book_html(stream, books[i], i == len - 1);
	fprintf(stream, "</ol>\n");
	if (!last)
		fprintf(stream, "\n\n");
}

void
print_book_plain(FILE *stream, struct book item, int last)
{
	fprintf(stream, "%s, \"%s\"\n", item.a, item.t);
	if (!last)
		fprintf(stream, "\n");
}

void
print_field_plain(FILE *stream, const char *field, const struct book *books, int len, int last)
{
	int i;
	fprintf(stream, "=== %s ===\n", field);
	for (i = 0; i < len; i++)
		print_book_plain(stream, books[i], i == len - 1);
	if (!last)
		fprintf(stream, "\n\n");
}

void
print_to_file(const char *filename, void (*printer)(FILE *stream, const char *field, const struct book *books, int len, int last))
{
	FILE *file;
	if (!(file = fopen(filename, "w"))) {
		fprintf(stderr, "Cannot open file %s.\n", filename);
		return;
	}
	printer(file, "Математика", math, sizeof(math) / sizeof(*math), 0);
	printer(file, "Физика", physics, sizeof(physics) / sizeof(*physics), 0);
	printer(file, "English", english, sizeof(english) / sizeof(*english), 1);
	fclose(file);
}

int
main()
{
	print_to_file(htmlfile, print_field_html);
	print_to_file(plainfile, print_field_plain);
	return 0;
}
