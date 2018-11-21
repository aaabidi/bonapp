require "application_system_test_case"

class HallsTest < ApplicationSystemTestCase
  setup do
    @hall = halls(:one)
  end

  test "visiting the index" do
    visit halls_url
    assert_selector "h1", text: "Halls"
  end

  test "creating a Hall" do
    visit halls_url
    click_on "New Hall"

    fill_in "Name", with: @hall.name
    click_on "Create Hall"

    assert_text "Hall was successfully created"
    click_on "Back"
  end

  test "updating a Hall" do
    visit halls_url
    click_on "Edit", match: :first

    fill_in "Name", with: @hall.name
    click_on "Update Hall"

    assert_text "Hall was successfully updated"
    click_on "Back"
  end

  test "destroying a Hall" do
    visit halls_url
    page.accept_confirm do
      click_on "Destroy", match: :first
    end

    assert_text "Hall was successfully destroyed"
  end
end
