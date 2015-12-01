json.array!(@goalsheets) do |goalsheet|
  json.extract! goalsheet, :id, :time, :goals
  json.url goalsheet_url(goalsheet, format: :json)
end
