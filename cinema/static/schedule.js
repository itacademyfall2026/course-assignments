(() => {
  'use strict';

  // Даты кинотеатра определяются по Минску, независимо от часового пояса зрителя.
  const cinemaDate = new Intl.DateTimeFormat('en-CA', {
    timeZone: 'Europe/Minsk',
    year: 'numeric',
    month: '2-digit',
    day: '2-digit',
  });
  const shortDate = new Intl.DateTimeFormat('ru-RU', {
    timeZone: 'UTC', day: 'numeric', month: 'long',
  });
  const fullDate = new Intl.DateTimeFormat('ru-RU', {
    timeZone: 'UTC', weekday: 'long', day: 'numeric', month: 'long',
  });
  const dateWithYear = new Intl.DateTimeFormat('ru-RU', {
    timeZone: 'UTC', day: 'numeric', month: 'long', year: 'numeric',
  });
  let lastDateKey = '';

  function updateDates() {
    const parts = Object.fromEntries(
      cinemaDate.formatToParts(new Date()).map(({ type, value }) => [type, value]),
    );
    const dateKey = `${parts.year}-${parts.month}-${parts.day}`;
    if (dateKey === lastDateKey) return;
    lastDateKey = dateKey;

    // UTC здесь хранит календарный день: прибавление дней не зависит от DST.
    const today = new Date(Date.UTC(+parts.year, +parts.month - 1, +parts.day));
    const dayAfter = (offset) => {
      const date = new Date(today);
      date.setUTCDate(date.getUTCDate() + offset);
      return date;
    };
    const dates = { today, tomorrow: dayAfter(1), 'day-after': dayAfter(2) };
    // «На неделю» — семь дней, включая сегодняшний.
    const weekEnd = dayAfter(6);
    const rangeFormatter = today.getUTCFullYear() === weekEnd.getUTCFullYear()
      ? shortDate : dateWithYear;
    const weekLabel = rangeFormatter.formatRange(today, weekEnd);

    document.querySelectorAll('[data-date]').forEach((element) => {
      const period = element.dataset.date;
      if (period === 'week') {
        element.textContent = weekLabel;
      } else if (dates[period]) {
        const formatter = element.dataset.dateFormat === 'full' ? fullDate : shortDate;
        const label = formatter.format(dates[period]);
        element.textContent = label[0].toLocaleUpperCase('ru-RU') + label.slice(1);
      }
    });
  }

  updateDates();
  // Обновляем открытую афишу после полуночи и возвращения во вкладку.
  window.setInterval(updateDates, 60_000);
  window.addEventListener('pageshow', updateDates);
  document.addEventListener('visibilitychange', () => {
    if (!document.hidden) updateDates();
  });
})();
