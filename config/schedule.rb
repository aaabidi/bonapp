#Automatically clears out the old food and adds the new ones at meal times

every 1.day at: '5am' do
  exec("python3 /scraper/WebScraper.py")
end

every :weekday, at: '7am' do
  Status.delete_all
  Review.delete_all
  Food.delete_all
  exec("rails runner /scraper/fribleyBreakfast")
  exec("rails runner /scraper/leutnerBreakfast")
end

every :weekday, at: '11am' do
  Status.delete_all
  Review.delete_all
  Food.delete_all
  exec("rails runner /scraper/fribleyLunch")
  exec("rails runner /scraper/leutnerLunch")
end

every 1.day at: '5pm' do
  Status.delete_all
  Review.delete_all
  Food.delete_all
  exec("rails runner /scraper/fribleyDinner")
  exec("rails runner /scraper/leutnerDinner")
end

every :saturday, at: '10am' do
  Status.delete_all
  Review.delete_all
  Food.delete_all
  exec("rails runner /scraper/fribleyBrunch")
  exec("rails runner /scraper/leutnerBrunch")
end

every :sunday, at: '10am' do
  Status.delete_all
  Review.delete_all
  Food.delete_all
  exec("rails runner /scraper/fribleyBrunch")
  exec("rails runner /scraper/leutnerBrunch")
end
